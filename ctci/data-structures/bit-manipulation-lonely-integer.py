#!/bin/python

import sys

def lonely_integer(a):
	ints = {}

	for elem in a:
		if elem not in ints:
			ints[elem] = 0

		if ints[elem] == 0:
			ints[elem] += 1

		else:
			ints[elem] = ints[elem] + (ints[elem]) * -1

	return [key for key, value in ints.iteritems() if value != 0][0]
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)

