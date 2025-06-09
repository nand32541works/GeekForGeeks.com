class Solution:
    def isDeadEnd(self, root):
        def check(n, left=0, right=float('inf')):
            if not n.left and not n.right:
                return n.data - 1 == left and n.data + 1 == right
            if n.left and check(n.left, left, n.data):
                return True
            if n.right and check(n.right, n.data, right):
                return True
            return False
        return check(root)
