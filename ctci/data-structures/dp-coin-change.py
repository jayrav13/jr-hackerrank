#!/bin/python

import sys

mem = []

def make_change(coins, n):
	global mem

	total = 0

	for i in coins:

		# Add all of the paths that resulted in a successful make_change
		if i < n:
			if (n - i) not in mem:
				total += make_change(coins, n - i)
				mem.append(n - i)

		# Because elements of n are unique, once you get here, return 1.
		elif n - i == 0:
			total += 1

	return total

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n) + 1

