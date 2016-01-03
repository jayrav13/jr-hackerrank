"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 return back the head of the linked list in the below method. 
"""

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def Delete(head, position):
	if position == 0:
		return head.next
	else:
		count = 0
		node = head
		while node != None:
			if count + 1 == position:
				rem = node.next
				node.next = node.next.next
				rem = None
			
			count = count + 1
			node = node.next

	return head
