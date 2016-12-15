#!/usr/bin/env python

import sys
import argparse

## To avoid getting "IOError: [Errno 32] Broken pipe" upon piping the output
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Print histgram in ASCII')
parser.add_argument('-s', '--step', dest='step_size', type=int, default=1, help='')
parser.add_argument('-r', '--reverse', action='store_true', help='print in descending order')

args = parser.parse_args()


def floor(val, step_size):
    return step_size * (int(val) / step_size)

def ceiling(val, step_size):
    return step_size * (int(val) / step_size + 1)

def stars(count, max_count):
    return '*' * count if max_count <= 50 else '*' * (50 * count / max_count)


vals = map(lambda x: float(x.strip()), sys.stdin.readlines())

min_val = min(vals)
max_val = max(vals)

min_bound = floor(min_val, args.step_size)
max_bound = ceiling(max_val, args.step_size)

freq = {}
for i in range(min_bound, max_bound, args.step_size):
    freq[i] = 0

for val in vals:
    step = floor(val, args.step_size)
    freq[step] = freq[step] + 1

max_count = max(freq.values())
for step, count in sorted(freq.items(), key=lambda x: x[0], reverse=args.reverse):
    print '%5d (%4d) %s' % (step, count, stars(count, max_count))
             
            
