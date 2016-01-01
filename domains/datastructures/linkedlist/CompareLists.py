"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
	fail = 0
	while(headA != None or headB != None):
		values = []
		if headA != None:
			values.append(headA.data)
		else:
			values.append(None)
		
		if headB != None:
			values.append(headB.data)
		else:
			values.append(None)

		if values[0] != values[1]:
			fail = fail + 1

		if headA != None:
			headA = headA.next
		if headB != None:
			headB = headB.next

	if fail != 0:
		return 0
	else:
		return 1
