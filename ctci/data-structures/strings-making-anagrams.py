"""
Making Anagrams

Jay Ravaliya
"""

def number_needed(a, b):

	base = None
	second = None
	totalLen = len(a) + len(b)
	count = 0

	if len(a) < len(b):
		base = a
		second = b
	else:
		base = b
		second = a

	for i in range(0, len(base)):
		if base[i] in second:
			count += 2
			second.replace(base[i], "")

	return totalLen - count

# Input strings
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

