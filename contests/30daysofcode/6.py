#!/bin/python

import sys

n = int(raw_input().strip())

for i in range(1, n + 1):
    for j in range(0, abs(i - n)):
        sys.stdout.write(" ")
    for j in range(0, i):
        sys.stdout.write("#")
    print "\n",
