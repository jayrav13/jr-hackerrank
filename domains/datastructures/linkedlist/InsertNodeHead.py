"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

return back the head of the linked list in the below method. 
""" 

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def Insert(head, data):
	if head == None:
		return Node(data)
	else:
		return Node(data, head)
