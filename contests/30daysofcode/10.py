n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

for elem in arr:
	soln = ""
	while elem >= 1:
		soln = soln + str(elem % 2)
		elem = elem / 2
	print soln[::-1]
