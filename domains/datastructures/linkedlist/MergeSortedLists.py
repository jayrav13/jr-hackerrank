"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 return back the head of the linked list in the below method.
"""

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def MergeLists(headA, headB):
	if headA == None:
		return headB
	if headB == None:
		return headA

	if headA.data < headB.data:
		headA.next = MergeLists(headA.next, headB)
		return headA
	else:
		headB.next = MergeLists(headA, headB.next)
		return headB


A = Node(10, Node(12, Node(14, Node(16, None))))
B = Node(11, Node(13, Node(15, Node(17, None))))

result = MergeLists(A, B)

while result != None:
	print result.data
	result = result.next
