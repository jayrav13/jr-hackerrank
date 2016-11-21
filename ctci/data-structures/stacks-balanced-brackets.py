def is_matched(expression):

	stack = []

	for elem in expression:
		if len(stack) == 0 or elem != complement(stack[-1]):
			stack.append(elem)
		else:
			stack.pop(len(stack) - 1)

	print stack

	return len(stack) == 0

def complement(char):
	open = ['(', '[', '{']
	close = [')', ']', '}']

	if char in open:
		return close[open.index(char)]
	else:
		return open[close.index(char)]

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

