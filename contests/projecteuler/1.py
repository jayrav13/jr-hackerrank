n = int(raw_input().strip())

arr = []

for i in range(0, n): 
        arr.append(int(raw_input().strip()))

for num in arr:
        print sum([i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]) 
