#!/usr/bin/env python3

import sys

def parse(line):
    return [s.strip() for s in line.split(';', maxsplit=1)]

def output(code_point, name):
    try:
        c = chr(int(code_point, 16))
    except ValueError:
        c = ''
    print(c, code_point, name, sep='\t')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: {} <search>')
        sys.exit(1)

    query = ' '.join(sys.argv[1:])

    with open('DerivedName.txt') as f:
        for line in (l.strip() for l in f):
            if not line or line[0] == '#':
                continue
            code_point, name = parse(line)
            if query.upper() in name:
                output(code_point, name)
