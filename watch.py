#!/usr/bin/env python3

import inotify.adapters
import inotify.constants
import os.path
import subprocess
import threading
import time

DIR = os.path.abspath(os.path.dirname(__file__))

TO_WATCH = {
    b'template.html': 'all',
    b'pandoc.css': 'all',
    b'index.md': ['index'],
    b'modules/module1.xSpnKKsf.md': ['module1'],
    b'modules/module2.1ze59Jg6.md': ['module2'],
    b'modules/module3.brjM6OTI.md': ['module3'],
    b'modules/module4.wA7dhLqP.md': ['module4'],
    b'modules/module5.jPQ8bPvi.md': ['module5'],
    b'modules/module6.wedUF8xu.md': ['module6'],
    b'modules/module7.czgnasyN.md': ['module7'],
}

PANDOC_COMMAND = [
    'pandoc',                      # executable
    None,                          # input filename
    '-o', None,                    # output output
    '-t', 'html5',                 # format to write
    '--smart',                     # smart quotes and hyphens
    '--template', 'template.html', # HTML template to use
    '--css', 'pandoc.css ',        # CSS to link to from the output
    '--highlight-style', 'tango',  # highlighting syntax for code sections
]

def make_pandoc_command(infile, outfile):
    result = PANDOC_COMMAND[:]
    result[1] = infile
    result[3] = outfile
    return result


JOBS = {
    'index':   make_pandoc_command('index.md',                    'out/index.html'),
    'module1': make_pandoc_command('modules/module1.xSpnKKsf.md', 'out/module1.xSpnKKsf.html'),
    'module2': make_pandoc_command('modules/module2.1ze59Jg6.md', 'out/module2.1ze59Jg6.html'),
    'module3': make_pandoc_command('modules/module3.brjM6OTI.md', 'out/module3.brjM6OTI.html'),
    'module4': make_pandoc_command('modules/module4.wA7dhLqP.md', 'out/module4.wA7dhLqP.html'),
    'module5': make_pandoc_command('modules/module5.jPQ8bPvi.md', 'out/module5.jPQ8bPvi.html'),
    'module6': make_pandoc_command('modules/module6.wedUF8xu.md', 'out/module6.wedUF8xu.html'),
    'module7': make_pandoc_command('modules/module7.czgnasyN.md', 'out/module7.czgnasyN.html'),
    'template': ['cp', 'template.html', 'out/template.html'],
    'css': ['cp', 'pandoc.css', 'out/pandoc.css'],
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
        job = subprocess.run(JOBS[job_name])
        
        if job.returncode < 0:
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