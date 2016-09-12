#!/usr/bin/env python3

import inotify.adapters
import inotify.constants
import os.path
import subprocess
import threading
import time

TO_WATCH = {
    b'pandoc.css':         ['css'],
    b'template.html':      ['index'],
    b'index.md':           ['index'],
    b'modules/module1.md': ['index'],
    b'modules/module2.md': ['index'],
    b'modules/module3.md': ['index'],
    b'modules/module4.md': ['index'],
    b'modules/module5.md': ['index'],
    b'modules/module6.md': ['index'],
    b'modules/module7.md': ['index'],
}

JOBS = {
    'index': [
        'pandoc',                      # executable
        'index.md',                    # input filenames
        'modules/module1.md',          #   -- ditto --
        'modules/module2.md',          #   -- ditto --
        'modules/module3.md',          #   -- ditto --
        'modules/module4.md',          #   -- ditto --
        'modules/module5.md',          #   -- ditto --
        'modules/module6.md',          #   -- ditto --
        'modules/module7.md',          #   -- ditto --
        '-o', 'index.html',            # output output
        '-t', 'html5',                 # format to write
        '--smart',                     # smart quotes and hyphens
        '--template', 'template.html', # HTML template to use
        '--css', 'pandoc.css ',        # CSS to link to from the output
        '--highlight-style', 'tango',  # highlighting syntax for code sections
    ],
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
        returncode = subprocess.call(JOBS[job_name])
        
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
