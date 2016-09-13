#!/usr/bin/env python3

import inotify.adapters
import inotify.constants
import os.path
import subprocess
import threading
import time

def add_lang(lang):
    job_name = '{}-index'.format(lang)
    
    TO_WATCH[b'template.html'].append(job_name)
    
    filename = '{}/index.md'.format(lang)
    TO_WATCH[filename.encode('ascii')] = [job_name]
    
    for i in range(7):
        module_num = i + 1
        filename = '{}/modules/module{}.md'.format(lang, module_num)
        TO_WATCH[filename.encode('ascii')] = [job_name]
    
    JOBS[job_name] = [make_pandoc_command(lang)]

def make_pandoc_command(lang):
    return (
        # executable
        'pandoc',
        
        # input filenames
        '{}/index.md'.format(lang),
        '{}/modules/module1.md'.format(lang),
        '{}/modules/module2.md'.format(lang),
        '{}/modules/module3.md'.format(lang),
        '{}/modules/module4.md'.format(lang),
        '{}/modules/module5.md'.format(lang),
        '{}/modules/module6.md'.format(lang),
        '{}/modules/module7.md'.format(lang),
        
        # output filename
        '-o', 'out/index-{}.html'.format(lang),
        
        # More options
        '-t', 'html5',                 # format to write
        '--smart',                     # smart quotes and hyphens
        '--template', 'template.html', # HTML template to use
        '--css', 'pandoc.css',         # CSS to link to from the output
        '--highlight-style', 'tango',  # highlighting syntax for code sections
    )

TO_WATCH = {
    b'pandoc.css':    ['css'],
    b'template.html': [],
}

JOBS = {
    'css': [('cp', 'pandoc.css', 'out/pandoc.css')],
}

add_lang('en')
add_lang('pt')


class Router(threading.Thread):
    
    def __init__(self, interval=1, sleep_for=1):
        super().__init__()
        
        self.prev = time.time() - interval
        self.interval = interval
        self.sleep_for = sleep_for
        
        self.queue = set(JOBS.keys())
    
    
    def push(self, path):
        job_names = TO_WATCH[path]
        
        if job_names == 'all':
            job_names = JOBS.keys()
            
        self.queue.update(job_names)
        
        self.prev = time.time()
    
    
    def process(self, job_name):
        job_list = JOBS[job_name]
        
        for job in job_list:
            returncode = subprocess.call(job)
            if returncode < 0:
                break
        
        if returncode < 0:
            print('did not make it')
        else:
            print()
    
    
    def process_queue(self):
        for job_name in self.queue:
            print('{!r} ... '.format(job_name), end='', flush=True)
            self.process(job_name)
            
        self.queue.clear()
    
    
    def run(self):
        self.running = True
        
        while self.running:
            if len(self.queue) > 0 and time.time() - self.prev > self.interval:
                self.process_queue()
            
            time.sleep(self.sleep_for)
    
    
    def stop(self):
        self.running = False


def add_watches(notifier):
    for filename in TO_WATCH:
        notifier.add_watch(filename, mask=inotify.constants.IN_CLOSE_WRITE)


def main():
    notifier = inotify.adapters.Inotify()
    add_watches(notifier)
    
    router = Router()
    router.daemon = True
    router.start()
    
    try:
        for event in notifier.event_gen():
            if event is not None:
                header, type_names, watch_path, filename = event
                router.push(watch_path)
    
    except KeyboardInterrupt:
        print()
    finally:
        router.stop()


if __name__ == '__main__':
    main()
