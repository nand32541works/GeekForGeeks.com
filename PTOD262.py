'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''
class Solution:
    def constructTree(self, pre, post):
        n = len(pre)
        preIndex = [0]  
        postIndexMap = {val: i for i, val in enumerate(post)}  
        def build(l, r):
            if preIndex[0] >= n or l > r:
                return None
            root = Node(pre[preIndex[0]])
            preIndex[0] += 1
            if l == r or preIndex[0] >= n:
                return root
            leftVal = pre[preIndex[0]]
            idx = postIndexMap[leftVal]
            root.left = build(l, idx)
            root.right = build(idx + 1, r - 1)
            return root
        return build(0, n - 1)
