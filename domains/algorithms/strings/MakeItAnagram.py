# Input letters
a = raw_input().strip()
b = raw_input().strip()

# Variables for finished, deletes
finished = []
deletes = 0

# For each letter, loop through and do deletes
for letter in a:
	if letter not in finished:
		deletes = deletes + abs(a.count(letter) - b.count(letter))
		finished.append(letter)

for letter in b:
	if letter not in finished:
		deletes = deletes + abs(b.count(letter) - a.count(letter))
		finished.append(letter)

print deletes
