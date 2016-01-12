#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while len(arr) != 0:
	minimum = min(arr)
	arr = [x - minimum for x in arr]
	print len(arr)
	arr = [x for x in arr if x != 0]
