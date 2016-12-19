#!/usr/bin/env python

import sys
import argparse

## To avoid getting "IOError: [Errno 32] Broken pipe" upon piping the output
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Force align columns')
parser.add_argument('-i', '--ifs', default='\t',   help='specify input field separator')
parser.add_argument('-o', '--ofs', default='    ', help='specify output field separator')
parser.add_argument('-a', '--align', choices=('l', 'r'), default='l', help="specify alignment, left 'l' or right 'r'")

args = parser.parse_args()

def calc_max_bytes(items):
    return max(map(len, items))

def extract_col_items(col_separated_lines, idx):
    return map(lambda x: x[idx], col_separated_lines)

lines = sys.stdin.readlines()
col_separated_lines = map(lambda x: x.strip().split(args.ifs), lines)
num_col = len(col_separated_lines[0])

max_bytes = []
for i in range(num_col):
    col_items = extract_col_items(col_separated_lines, i)
    max_bytes.append(calc_max_bytes(col_items))

if args.align == 'l':
    fmt = args.ofs.join(map(lambda x: '%-' + str(x) + 's', max_bytes))
else:
    fmt = args.ofs.join(map(lambda x: '%' + str(x) + 's', max_bytes))

for items in col_separated_lines:
    print fmt % tuple(items)
