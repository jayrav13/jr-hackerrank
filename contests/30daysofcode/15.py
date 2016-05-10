def insert(self,head,data):
	if head == None:
		head = Node()
		head.data = data
		head.next = None
		return head
	else:
		node = head
		while node.next != None:
			node = node.next
			node.next = Node()
			node.next.data = data
			node.next.next = None
			return head
#Complete this method
