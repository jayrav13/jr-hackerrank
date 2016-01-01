#!/bin/python

import sys

n = int(raw_input().strip())
a = []

for x in range(0, n):
	a_temp = map(int, raw_input().strip().split(' '))
	a.append(a_temp)


track = [0, n-1]
result = [0,0]

for x in range(0, len(a)):
	result[0] = result[0] + a[x][track[0]]
	result[1] = result[1] + a[x][track[1]]
	track[0] = track[0] + 1
	track[1] = track[1] - 1

print abs(result[0] - result[1])
