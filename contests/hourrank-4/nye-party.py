n = int(raw_input().strip())

arr = raw_input().strip().split(' ')

for i in range(0, len(arr)):
	arr[i] = int(arr[i])

count = 0
for i in range(0, len(arr)):
	if i == 0:
		count = arr[i]
	else:
		if arr[i] == arr[i - 1]:
			count = count + 1
		else:
			if count > arr[i]:
				count = count + 1
			else:
				count = arr[i]

print count
