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

	done = False
	head = None

	while(done == False):
		if headA == None and headB == None:
			done = True
			break
		
		headAData = None
		headBData = None

		if headA != None:
			headAData = headA.data
		if headB != None:
			headBData = headB.data

#		print "headA:" + str(headA.data)
#		print "headB:" + str(headB.data)

		if headAData < headBData:
			if head == None:
				head = Node(headAData)
			else:
				head.next = Node(headAData)
				head = head.next

			try:
				headA = headA.next
			except:
				headA = None

		else:
			if head == None:
				head = Node(headBData)
			else:
				head.next = Node(headBData)
				head = head.next

			try:
				headB = headB.next
			except:
				headB = None

		if headA == None and headB == None:
			done = True

		print head.data

	return head


headA = Node(10)
headA.next = Node(12)
headA.next.next = Node(14)

headB = Node(11)
headB.next = Node(13)
headB.next.next = Node(15)

head = MergeLists(headA, headB)
