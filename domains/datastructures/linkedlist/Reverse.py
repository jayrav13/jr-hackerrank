"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
	if head == None or head.next == None:
		return head
	else:
		prev = None
		while(head.next != None):
			temp = head.next
			head.next = prev
			prev = head
			head = temp

		head.next = prev

		return head
