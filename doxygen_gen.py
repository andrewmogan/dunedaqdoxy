#!/usr/bin/env python

import os, sys
import argparse
from os.path import isdir, join

def main(source_dir, build_dir):
    source_dirs = [join(source_dir, p) for p in os.listdir(source_dir) if isdir(join(source_dir, p))]
    build_dirs = [join(build_dir, p) for p in os.listdir(build_dir) if isdir(join(build_dir, p)) and p!='CMakeFiles']
    dirs = source_dirs + build_dirs

    with open("Doxyfile.in", 'r') as f:
        doxyfile = f.read()

    # doxyfile.replace('@INPUT_LIST', str(dirs))
    input_list = ['']
    for d in dirs:
        input_list += [
            join(d, s) for s in ['include', 'src', 'pybindsrc', 'apps', 'docs', 'python', 'scripts', 'codegen']
        ]

    # print(' \\\n'.join(input_list))
    doxyfile = doxyfile.replace('@INPUT_LIST', ' \\\n'.join(input_list))

    with open("Doxyfile", 'w') as f:
        f.write(doxyfile)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Script to write input directories to the INPUT field of Doxyfile.in,
        then save as Doxyfile. This allows the command `doxygen` to be run.
        """)
    dbt_area_root = os.getenv('DBT_AREA_ROOT')
    if dbt_area_root is None:
        print("Error: The environment variable DBT_AREA_ROOT is not set. Exiting...")
        sys.exit(1)
    parser.add_argument('--source_dir', type=str, default=join(dbt_area_root, 'sourcecode'), 
                        help='Path to sourcecode directory in a dbt environment')
    parser.add_argument('--build_dir', type=str, default=join(dbt_area_root, 'build'), 
                        help='Path to build directory in a dbt environment')
    args = parser.parse_args()
    main(args.source_dir, args.build_dir)