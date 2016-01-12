n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append([long(x) for x in raw_input().strip().split(' ')])

for elem in arr:
	count = 0
	start = elem[0]
	end = elem[1]

	while start <= end:
		if float(long(start**0.5)) == float(start**0.5):	
			count = count + 1

		if count == 0:
			start = start + 1
		else:
			start = ((start**0.5) + 1)**2

	print count
