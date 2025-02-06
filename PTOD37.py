#THis code is written in Python

class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder: return None
        root, mid = Node(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree(inorder[:mid],preorder[1:mid+1])
        root.right = self.buildTree(inorder[mid+1:],preorder[mid+1:])
        return root
