#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Format for markdown table')
parser.add_argument('-d', '--delimiter', dest='delim', default=None, help='specify input delimiter')
parser.add_argument('-H', '--header', action='store_true', help='treat first line as header')
parser.add_argument('-a', '--align', help='specify alignment of the columns (use with -H option). e.g. -a lcr')

args = parser.parse_args()


def join_by_bar(items):
    return '| ' + ' | '.join(items) + ' |'

def format(line):
    return join_by_bar(line.strip().split(args.delim))

def replace_align_char(c):
    if c == 'l':
        return ':---'
    elif c == 'c':
        return ':---:'
    elif c == 'r':
        return '---:'
    else:
        sys.exit("Error: Only 'l', 'c', 'r' are accepted as an alignment specifier.")

def header_line(num_fields):
    if args.align:
        align_chars = args.align
        if len(align_chars) != num_fields:
            sys.exit('Error: Number of alignment specifiers did not match the number of fields. %d given for %d.' % (len(align_chars), num_fields))
        alignments = map(replace_align_char, align_chars)
    else:
        alignments = ['---'] * num_fields
    return join_by_bar(alignments)

def num_field(line):
    return len(line.split(args.delim))


if args.header:
    line = sys.stdin.readline()
    header_line = header_line(num_field(line))
    print format(line)
    print header_line

for line in sys.stdin.readlines():
    print format(line)

