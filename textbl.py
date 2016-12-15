#!/usr/bin/env python

import sys
import argparse
import re

## To avoid getting "IOError: [Errno 32] Broken pipe" upon piping the output
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Format in latex table')
parser.add_argument('-d', '--delimiter', dest='delim', default='\t', help='input field separator')

args = parser.parse_args()

def format(line):
    return ' & '.join(line.strip().split(args.delim)) + ' \\\\'

for line in sys.stdin.readlines():
    print format(line)
