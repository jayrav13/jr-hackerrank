#!/bin/python

import sys

time = raw_input().strip()

timearr = time.split(':')

timearr[2] = [timearr[2][0:2], timearr[2][2:4]]

if timearr[2][1] == 'PM':
	timearr[0] = int(timearr[0]) + 12

if timearr[2][0] == 'AM' and timearr[0] == "12":
	timearr[0] = "00"

print str(timearr[0]) + ":" + str(timearr[1]) + ":" + str(timearr[2][0])
