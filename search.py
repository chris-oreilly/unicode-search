#!/usr/bin/env python3

from collections import namedtuple
import sys

Entry = namedtuple('Entry', ['code', 'name'])

def parse(line):
    parts = [s.strip() for s in line.split(';', maxsplit=1)]
    return Entry(*parts)

def match(query, entry):
    for term in query:
        if term.upper() not in entry.name:
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
        print('usage: {} <search>'.format(sys.argv[0]))
        sys.exit(1)

    query = sys.argv[1:]

    with open('DerivedName.txt') as f:
        for line in f:
            if not line.strip() or line[0] == '#':
                continue
            entry = parse(line)
            if match(query, entry):
                output(entry)
