#!/bin/python

import sys

time = raw_input().strip().split(':')

if time[2][-2:] == 'PM' and int(time[0]) < 12:
	time[0] = str(int(time[0]) + 12)
if time[2][-2:] == 'AM':
	if time[0] == '12':
		time[0] = '00'

if int(time[0]) == 24:
	time[0] = "00"

time[2] = time[2][:-2]

print ":".join(time)
