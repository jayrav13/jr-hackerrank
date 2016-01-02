n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

def prime_factors(num):
	result = []
	divisor = 2
	while num is not 1:
		if num % divisor == 0:
			result.append(divisor)
			num = num / divisor
			divisor = 2
		else:
			divisor = divisor + 1
	return result

def all_prime_factors(num):
	return [prime_factors(i) for i in range(2, num + 1)]

def count_instances(factors, num):
	result = [0 for i in range(0, num)]
	for elem in factors:
		for i in range(1, num + 1):
			if elem.count(i) > result[i - 1]:
				result[i - 1] = elem.count(i)

	return result

def smallest_multiple(counts):
	product = 1
	for i, v in enumerate(counts):
		product = product * (i + 1) ** v
	return product
		

for elem in arr:
	print smallest_multiple(count_instances(all_prime_factors(elem), elem))
