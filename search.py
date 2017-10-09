#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: {} <search>')
        sys.exit(1)

    query = ' '.join(sys.argv[1:])

    with open('DerivedName.txt') as f:
        for line in (l.strip() for l in f):
            if not line or line[0] == '#' or '*' in line:
                continue
            code_point, name = [s.strip() for s in line.split(';', 1)]
            if query.upper() in name:
                print(chr(int(code_point, 16)), code_point, name, sep='\t')
