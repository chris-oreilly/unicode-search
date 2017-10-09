#!/usr/bin/env python3

from collections import namedtuple
import sys

Entry = namedtuple('Entry', ['code', 'name'])

def parse(line):
    parts = [s.strip() for s in line.split(';', maxsplit=1)]
    return Entry(*parts)

def match(entry, include, exclude=[]):
    for term in include:
        if term.upper() not in entry.name:
            return False
    for term in exclude:
        if term.upper() in entry.name:
            return False
    return True

def output(entry):
    try:
        c = chr(int(entry.code, 16))
    except ValueError:
        c = ''
    print(c, entry.code, entry.name, sep='\t')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: {} [+]include... -exclude...'.format(sys.argv[0]))
        sys.exit(1)

    include = []
    exclude = []
    for arg in sys.argv[1:]:
        if arg[0] == '-':
            exclude.append(arg[1:])
        elif arg[0] == '+':
            include.append(arg[1:])
        else:
            include.append(arg)

    with open('DerivedName.txt') as f:
        for line in f:
            if not line.strip() or line[0] == '#':
                continue
            entry = parse(line)
            if match(entry, include, exclude):
                output(entry)
