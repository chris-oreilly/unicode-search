#!/usr/bin/env python3

import sys

def parse(line):
    return [s.strip() for s in line.split(';', 1)]

def expand(code_points, name):
    if '..' in code_points:
        start, end = [int(s, 16) for s in code_points.split('..', 1)]
        for code_point in (str(s) for s in range(start, end + 1)):
            yield code_point, name.replace('*', code_point)
    else:
        yield code_points, name

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: {} <search>')
        sys.exit(1)

    query = ' '.join(sys.argv[1:])

    with open('DerivedName.txt') as f:
        for line in (l.strip() for l in f):
            if not line or line[0] == '#':
                continue
            for code_point, name in expand(*parse(line)):
                if query.upper() in name:
                    print(chr(int(code_point, 16)), code_point, name, sep='\t')
