#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

max = None

for x in range(0, 4):
	for y in range(0, 4):

		result = []
		works = 0

		for a in range(0, 3):
			for b in range(0, 3):
				result.append(arr[x + a][y + b])

		resultSum = sum(result) - result[3] - result[5]

		if max == None:
			max = resultSum
		if (sum(result) - result[3] - result[5]) > max:
			max = resultSum


if max != None:
	print max
