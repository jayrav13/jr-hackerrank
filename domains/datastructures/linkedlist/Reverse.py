"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
  return back the head of the linked list in the below method.
"""

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def Reverse(head):
	if head == None:
		return head
	else:
		last = None
		current = head

		while current != None:
			next = current.next
			current.next = last
			last = current
			current = next

	return last

node = Node(10)
node.next = Node(12)
node.next.next = Node(14)
node.next.next.next = Node(16)

result = Reverse(node)

while result != None:
	print result.data
	result = result.next
