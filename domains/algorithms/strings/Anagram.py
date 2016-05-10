n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(raw_input().strip())

for elem in arr:
	if len(elem) % 2 == 1:
		print -1
	else:
		words = [elem[0:(len(elem)/2)], elem[len(elem)/2:len(elem)]]
		done = []
		count = 0
		for elem in words[0]:
			if elem not in done:
				count = abs(words[0].count(elem) - words[1].count(elem)) + count
				done.append(elem)
		for elem in words[1]:
			if elem not in done:
				count = abs(words[0].count(elem) - words[1].count(elem)) + count
				done.append(elem)

		print count/2
