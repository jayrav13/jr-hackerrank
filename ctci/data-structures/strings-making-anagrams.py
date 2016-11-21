"""
Making Anagrams

Jay Ravaliya
"""

def number_needed(a, b):
	chars = {}

	for elem in a:
		if elem not in chars:
			chars[elem] = 0
		chars[elem] += 1
	for elem in b:
		if elem not in chars:
			chars[elem] = 0
		chars[elem] -= 1

	return sum([abs(x) for x in chars.values()])

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

