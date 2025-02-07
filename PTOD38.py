#This code is written in Python

class Solution:
    def inOrder(self,root):
        if not root:
            return []
        return self.inOrder(root.left)+[root.data]+self.inOrder(root.right)
