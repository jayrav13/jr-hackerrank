n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

for elem in arr:
	su = long(sum([x for x in range(1, elem + 1)])**2)
	sq = long(sum([x**2 for x in range(1, elem + 1)]))
	print su - sq
