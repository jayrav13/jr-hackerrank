""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):

	count = 2

	# Leaf node - if we reached here, return True and traverse back
	if root.left == None and root.right == None:
		return True

	if root.left is not None and root.left.data >= root.data:
		count -= 1

	if root.right is not None and root.right.data <= root.data:
		count -= 1

	return count == 2 and (root.left is not None and check_binary_search_tree_(root.left)) and (root.right is not None and check_binary_search_tree_(root.right))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
"""

root = Node(3)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)

print check_binary_search_tree_(root)
