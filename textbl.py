#!/usr/bin/env python

import sys
import argparse
import re

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Format in latex table')
parser.add_argument('-d', '--delimiter', dest='delim', default='\t', help='input field separator')

args = parser.parse_args()

def format(line):
    return ' & '.join(line.strip().split(args.delim)) + ' \\\\'

for line in sys.stdin.readlines():
    print format(line)
