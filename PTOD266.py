'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandyUtil(self, root, ans):
        if root is None:
            return 0
        l = self.distCandyUtil(root.left, ans)
        r = self.distCandyUtil(root.right, ans)
        ans[0] += abs(l) + abs(r)
        return root.data + l + r - 1
    def distCandy(self, root):
        ans = [0]
        self.distCandyUtil(root, ans)
        return ans[0]
