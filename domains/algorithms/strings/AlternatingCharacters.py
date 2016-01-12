n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(raw_input().strip())

for elem in arr:
	soln = []
	for letter in elem:
		if len(soln) == 0:
			soln.append(letter)
		elif soln[-1] != letter:
			soln.append(letter)

	print len(elem) - len("".join(soln))
