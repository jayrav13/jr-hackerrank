#!/bin/python

import sys

n = int(raw_input().strip())

for x in range(0, n):
	for y in range(0, n-x-1):
		sys.stdout.write(' ')
	for y in range(0, x+1):
		sys.stdout.write('#')
	print
