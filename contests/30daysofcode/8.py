# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())

arr = {}

for i in range(0, n):
	key = raw_input().strip()
	value = raw_input().strip()
	arr[key] = value

queries = []

while True:
	try:
		queries.append(raw_input().strip())
	except EOFError:
		break

for elem in queries:
	if elem in arr:
		print elem + "=" + arr[elem]
	else:
		print "Not found"
