class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):

		if root.left is None and root.right is None:
            return 0

        left = right = 0

        if root.left is not None:
            left = 1 + self.getHeight(root.left)

        if root.right is not None:
            right = 1 + self.getHeight(root.right)

        greater = 0

        if left > right:
            greater = left
        else:
            greater = right

        return greater

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
