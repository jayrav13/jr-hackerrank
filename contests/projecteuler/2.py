n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

for elem in arr:
	first = 1
	second = 2
	result = 0
	while second < elem:
		temp = second
		second = second + first
		first = temp
		if first % 2 == 0:
			result = result + first

	print result
