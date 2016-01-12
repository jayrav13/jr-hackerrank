#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))

ee = []

for a0 in xrange(t):
	i,j = raw_input().strip().split(' ')
	i,j = [int(i),int(j)]
	ee.append([i, j])

for elem in ee:
	print min(width[elem[0]:elem[1]+1])
