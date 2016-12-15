#!/usr/bin/env python

import sys
import argparse

## To avoid getting "IOError: [Errno 32] Broken pipe" upon piping the output
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Group and count')

args = parser.parse_args()

count_table = {}

for line in sys.stdin.readlines():
    key = line.strip()
    count_table[key] = count_table.setdefault(key, 0) + 1
    
for key, count in sorted(count_table.items(), key=lambda x: x[1], reverse=True):
    print '%s\t%d' % (key, count)

