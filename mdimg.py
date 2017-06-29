#!/usr/bin/env python

import sys
import argparse
import re

## To avoid getting "IOError: [Errno 32] Broken pipe" upon piping the output
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Format for markdown table')
parser.add_argument('md_str', help='markdown string e.g. ![foo](bar)')
parser.add_argument('-w', '--width', type=int, help='width')

args = parser.parse_args()

html_str = re.sub(r"\[(.+)\]\((.+)\)", r'<img src="\2" alt="\1"', args.md_str)
if args.width:
    html_str += " width=%d>" % args.width
else:
    html_str += ">"

print html_str
