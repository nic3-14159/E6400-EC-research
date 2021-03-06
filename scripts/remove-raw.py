#!/bin/python
"""
    Takes in a parsed lpc dump and removes the hex dump
"""
import re
import sys

for line in sys.stdin:
    if (line.isspace()):
        print(line, end='')
    else:
        match = re.search(r"(Read|Write).*$|#.*$", line)
        print(match.group())
