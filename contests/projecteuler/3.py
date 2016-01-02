n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

def is_prime(num):
	count = 0
	for elem in range(2, num):
		if num % elem == 0:
			count = count + 1
	return count == 0

for elem in arr:
	result = -1
	for num in range(elem, 1, -1):
		if elem % num == 0 and is_prime(num) and elem is not num:
			result = num
			break

	if result == -1:
		result = elem

	print result
