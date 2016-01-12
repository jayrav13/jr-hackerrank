# Grab string
s = raw_input().strip()

# String Length, Unique Array
strlen = len(s)

# Generate output
results = {}
for elem in s:
	if elem in results:
		results[elem] = results[elem] + 1
	else:
		results[elem] = 1

for key, value
