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

def InsertNth(head, data, position):
	if position == 0 or head == None:
		return Node(data, head)
	else:
		node = head
		count = 0
		while(node.next != None):
			count = count + 1
			if count == position:
				new = Node(data)
				new.next = node.next
				node.next = new
			
			node = node.next

		if count < position:
			node.next = Node(data)

	return head
