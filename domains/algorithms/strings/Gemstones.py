n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(raw_input().strip())

tester = arr[0]
arr.pop(0)

total_count = 0

unique = []
for letter in tester:
	if letter not in unique:
		unique.append(letter)

for letter in unique:
	letter_count = 0
	for string in arr:
		if letter in string:
			letter_count = letter_count + 1

	if letter_count == len(arr):
		total_count = total_count + 1

print total_count
		

		

