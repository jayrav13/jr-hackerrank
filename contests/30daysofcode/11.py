#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
	arr_temp = map(int,raw_input().strip().split(' '))
	arr.append(arr_temp)

max = None

for i in range(0, 4):
	for j in range(0, 4):
		# For clarity - I summed up the entire square and then explicitly subtracted the two components not a part of the hour glass shape.
		sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] - arr[i + 1][j] - arr[i + 1][j + 2]
		if sum > max:
			max = sum

print max
