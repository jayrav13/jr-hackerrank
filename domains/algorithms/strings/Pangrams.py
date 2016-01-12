s = raw_input().strip().lower()

letters = list('abcdefghijklmnopqrstuvwxyz')

for elem in s:
	if elem in letters:
		letters.pop(letters.index(elem))

if len(letters) == 0:
	print "pangram"
else:
	print "not pangram"
