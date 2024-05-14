#!/usr/bin/env python

import os
from os.path import isdir, join

def main():
    print("xxx")
    src_dir = 'sourcecode/'
    dirs = [ join(src_dir, p) for p in os.listdir(src_dir) if isdir(join(src_dir, p))]
    

    with open("Doxyfile.in", 'r') as f:
        doxyfile = f.read()

    # doxyfile.replace('@INPUT_LIST', str(dirs))
    input_list = ['']
    for d in dirs:
        input_list += [
            join(d, s) for s in ['include', 'src', 'pybindsrc', 'apps', 'docs', 'python', 'scripts']
        ]

    # print(' \\\n'.join(input_list))
    doxyfile = doxyfile.replace('@INPUT_LIST', ' \\\n'.join(input_list))

    with open("Doxyfile", 'w') as f:
        f.write(doxyfile)



if __name__ == '__main__':
    main()