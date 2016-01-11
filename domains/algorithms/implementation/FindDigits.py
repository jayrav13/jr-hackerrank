n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

for elem in arr:
	val = str(elem)
	count = 0
	for letter in val:
		if int(letter) is not 0 and elem % int(letter) == 0:
			count = count + 1

	print count
