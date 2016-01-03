"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as

 return back the head of the linked list in the below method.
"""
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

  
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
	node = head
	if node == None:
		return Node(data)
	elif position == 0:
		return Node(data, head)
	else:
		count = 0
		while node.next != None:
			if count + 1 == position:
				new = Node(data, node.next)
				node.next = new
				return head
			count = count + 1
			node = node.next

		node.next = Node(data)
		return head
