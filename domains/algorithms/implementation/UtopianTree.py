n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(int(raw_input().strip()))

for elem in arr:
	height = 1
	is_spring = True
	for i in range(0, elem):
		if is_spring:
			height = (height * 2)
		else:
			height = height + 1
		is_spring = not is_spring
	print height
