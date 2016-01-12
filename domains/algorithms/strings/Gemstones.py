n = int(raw_input().strip())

arr = []

for i in range(0, n):
	arr.append(raw_input().strip())

largest = -1

for index, elem in enumerate(arr):
	if len(elem) > largest:
		largest = index

count = 0
largest = arr[largest]
minimum = []

for elem in arr:
	track = 0
	for letter in largest:
		if letter in elem:
			track = track + 1

	minimum.append(track)

print min(minimum)
