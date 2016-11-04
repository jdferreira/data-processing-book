#!/usr/bin/env python3

import sys
import os
import difflib

MODULES = [1, 2, 3, 4, 5, 6, 7]
MASTER_LANG = 'pt'
LANGS = ['en']

class CodeLine:
    
    def __init__(self, filename, line_no, line):
        self.filename = filename
        self.line_no = line_no
        self.line = line
    
    def __eq__(self, other):
        return self.line == other.line
    
    def __hash__(self):
        return hash(self.line)


def get_code(filename):
    in_code = False
    lang = None
    
    with open(filename) as f:
        for line_no, line in enumerate(f):
            line = line.rstrip('\n')
            
            code_markup = line.lstrip().startswith('```')
            should_yield = in_code or code_markup
            
            if code_markup:
                in_code = not in_code
                
                if in_code:
                    lang = line.strip()[3:]
            
            if in_code and lang == 'python':
                pos = line.find('#')
                if pos > -1:
                    line = line[:pos].rstrip()
                    if not line.strip():
                        should_yield = False
            
            if should_yield:
                yield CodeLine(filename, line_no + 1, line)

def diff_code(master, code):
    diff = difflib.SequenceMatcher(a=master, b=code)
    
    for tag, i1, i2, j1, j2 in diff.get_opcodes():
        if tag == 'equal':
            continue
        
        text_a = ''.join(i.line for i in diff.a[i1:i2]).strip()
        text_b = ''.join(i.line for i in diff.b[j1:j2]).strip()
        
        if text_a == '' and text_b == '':
            continue
        
        yield (i1, i2, j1, j2)


for module_number in MODULES:
    master_filename = os.path.join(MASTER_LANG, 'module{}.md'.format(module_number))
    master_code = list(get_code(master_filename))
    
    for lang in LANGS:
        filename = os.path.join(lang, 'module{}.md'.format(module_number))
        code = list(get_code(filename))
        
        diff_found = False
        
        for i1, i2, j1, j2 in diff_code(master_code, code):
            if not diff_found:
                print('Diff between {} and {}:'.format(master_filename, filename))
                diff_found = True
            
            print('<<< l.{}'.format(master_code[i1].line_no))
            print('\n'.join('    {}'.format(line.line) for line in master_code[i1:i2]))
            print('>>> l.{}'.format(code[j1].line_no))
            print('\n'.join('    {}'.format(line.line) for line in code[j1:j2]))
        
