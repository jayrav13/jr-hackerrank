"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
	if head == None or head.next_node == None:
		return 0

	first = head
	second = head.next_node

	while first is not None and second is not None:
		if first.data == second.data:
			return 1	

		first = first.next_node
		second = second.next_node

		if second is not None:
			second = second.next_node

	return 0
   
class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

n = None(10, None)
n.next_node = None
n = Node(10, Node(20, Node(30, Node(40, Node(20, None)))))
print has_cycle(n)

