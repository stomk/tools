#!/bin/bash

cat - | sed 's/[[:space:]]/ \| /g' | sed 's/^\(.*\)$/\| \1 \|/'

