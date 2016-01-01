#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for x in range(len(arr), 0, -1):
	print arr[x - 1],
