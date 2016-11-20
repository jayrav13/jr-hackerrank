"""
Left Rotation

Jay Ravaliya
"""

def array_left_rotation(a, n, k):
	output = []

	for i in range(k, n):
		output.append(a[i])

	for i in range(0, k):
		output.append(a[i])

	return output


# n = number of elements
# k = rotation number
n, k = map(int, raw_input().strip().split(' '))

# a = list of numbers
a = map(int, raw_input().strip().split(' '))

# Answer
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

