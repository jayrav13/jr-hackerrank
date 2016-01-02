n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

def is_palindrome(string):
	return string == string[::-1]

multiplications = [x * y for x in range(100, 1000) for y in range(100, 1000)]
multiplications = sorted(multiplications)

palindromes = []

for elem in multiplications:
	if is_palindrome(str(elem)):
		palindromes.append(elem)

for elem in arr:
	max_value = 0
	for val in reversed(palindromes):
		if is_palindrome(str(val)) and val < elem:
			print val
			break
