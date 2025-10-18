class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getKClosest(self, root, target, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)
            
        values = inorder(root)
        values.sort(key=lambda x: (abs(x - target), x))
        return values[:k]
