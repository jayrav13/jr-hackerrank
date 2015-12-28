"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
	if position == 0:
		return head.next
	else:
		node = head
		count = 0
		while(node.next != None):
			if count + 1 == position:
				delete = node.next
				node.next = delete.next
				return head

			count = count + 1
			node = node.next
