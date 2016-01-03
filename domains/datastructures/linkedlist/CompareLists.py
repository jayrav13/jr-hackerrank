"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
  return back the head of the linked list in the below method.
"""
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def CompareLists(headA, headB):
	count = 0

	while headA != None or headB != None:
		if (headA == None and headB != None) or (headA != None and headB == None):
			return 0

		if headA.data != headB.data:
			count = count + 1

		headA = headA.next
		headB = headB.next

	if count == 0:
		return 1
	else:
		return 0

