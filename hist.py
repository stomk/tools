#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Prints histgram in text format')
parser.add_argument('-s', '--step_size', type=int, default=1, help='')

args = parser.parse_args()


def floor(val, step_size):
    return step_size * (int(val) / step_size)

def ceiling(val, step_size):
    return step_size * (int(val) / step_size + 1)

def stars(count, max_count):
    return '*' * (50 * count / max_count)


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
for step, count in sorted(freq.items(), key=lambda x: x[0]):
    print '%5d (%4d) %s' % (step, count, stars(count, max_count))
             
            
