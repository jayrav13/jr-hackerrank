n = int(raw_input().strip())

arr = []
letters = list('abcdefghijklmnopqrstuvwxyz')

for i in range(0, n):
	arr.append(raw_input().strip())

for elem in arr:
	rev = elem[::-1]
	count = 0
	for i in range(0, len(rev)-1):
		if abs(letters.index(rev[i]) - letters.index(rev[i + 1])) != abs(letters.index(elem[i]) - letters.index(elem[i + 1])):
			count = count + 1

	if count > 0:
		print "Not Funny"
	else:
		print "Funny"
