#!/usr/bin/env python3

import inotify.adapters
import inotify.constants
import os.path
import subprocess
import threading
import time

TO_WATCH = {
    b'pandoc.css':         ['css'],
    b'template.html':      ['en-index', 'pt-index'],
    b'en/index.md':           ['en-index'],
    b'en/modules/module1.md': ['en-index'],
    b'en/modules/module2.md': ['en-index'],
    b'en/modules/module3.md': ['en-index'],
    b'en/modules/module4.md': ['en-index'],
    b'en/modules/module5.md': ['en-index'],
    b'en/modules/module6.md': ['en-index'],
    b'en/modules/module7.md': ['en-index'],
    # b'pt/index.md':           ['pt-index'],
    # b'pt/modules/module1.md': ['pt-index'],
    # b'pt/modules/module2.md': ['pt-index'],
    # b'pt/modules/module3.md': ['pt-index'],
    # b'pt/modules/module4.md': ['pt-index'],
    # b'pt/modules/module5.md': ['pt-index'],
    # b'pt/modules/module6.md': ['pt-index'],
    # b'pt/modules/module7.md': ['pt-index'],
}

JOBS = {
    'en-index': (
        'pandoc',                      # executable
        'en/index.md',                 # input filenames
        'en/modules/module1.md',       #   -- ditto --
        'en/modules/module2.md',       #   -- ditto --
        'en/modules/module3.md',       #   -- ditto --
        'en/modules/module4.md',       #   -- ditto --
        'en/modules/module5.md',       #   -- ditto --
        'en/modules/module6.md',       #   -- ditto --
        'en/modules/module7.md',       #   -- ditto --
        '-o', 'out/en/index.html',     # output output
        '-t', 'html5',                 # format to write
        '--smart',                     # smart quotes and hyphens
        '--template', 'template.html', # HTML template to use
        '--css', '../pandoc.css',      # CSS to link to from the output
        '--highlight-style', 'tango',  # highlighting syntax for code sections
    ),
    # 'pt-index': (
    #     'pandoc',                      # executable
    #     'en/index.md',                 # input filenames
    #     'en/modules/module1.md',       #   -- ditto --
    #     'en/modules/module2.md',       #   -- ditto --
    #     'en/modules/module3.md',       #   -- ditto --
    #     'en/modules/module4.md',       #   -- ditto --
    #     'en/modules/module5.md',       #   -- ditto --
    #     'en/modules/module6.md',       #   -- ditto --
    #     'en/modules/module7.md',       #   -- ditto --
    #     '-o', 'out/pt/index.html',     # output output
    #     '-t', 'html5',                 # format to write
    #     '--smart',                     # smart quotes and hyphens
    #     '--template', 'template.html', # HTML template to use
    #     '--css', '../pandoc.css',      # CSS to link to from the output
    #     '--highlight-style', 'tango',  # highlighting syntax for code sections
    # ),
    'css': ('cp', 'pandoc.css', 'out/pandoc.css'),
}


class Router(threading.Thread):
    
    def __init__(self, interval=1):
        super().__init__()
        
        self.prev = time.time()
        self.interval = interval
        
        self.queue = set(JOBS.keys())
    
    
    def push(self, path):
        job_names = TO_WATCH[path]
        
        if job_names == 'all':
            job_names = JOBS.keys()
            
        self.queue.update(job_names)
    
    
    def process(self, job_name):
        job_list = JOBS[job_name]
        if type(job_list) is tuple:
            job_list = [job_list]
        
        if len(job_list) == 0:
            return
        
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
            if self.running and len(self.queue) > 0:
                self.process_queue()
            
            time.sleep(self.interval)
    
    
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
