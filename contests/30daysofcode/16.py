n = int(raw_input().strip())

arr = [int(x) for x in raw_input().strip().split(' ')]

def insertionSort(alist):
	for index in range(1,len(alist)):

		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1

		alist[position]=currentvalue
	return alist

def sort(arr):
	swaps = -1
	while(swaps != 0):
		swaps = 0
		for x in range(0, len(arr) - 1):
			if arr[x] > arr[x + 1]:
				temp = arr[x]
				arr[x] = arr[x + 1]
				arr[x + 1] = temp
				swaps = swaps + 1

	return arr

arr = insertionSort(arr)

values = []
max_diff = float('inf')

for x in range(0, len(arr)-1):
	this_diff = abs(arr[x] - arr[x + 1])
	if(this_diff <= max_diff):
		if(this_diff < max_diff):
			values = [arr[x], arr[x + 1]]
		else:
			values.extend(arr[x], arr[x + 1])
		max_diff = this_diff

for elem in values:
	print elem,
