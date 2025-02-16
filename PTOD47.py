#This code is written in Python

class Solution:
    def serialize(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            ans.append(str(node.data) if node else 'N')
            if node:
                q.append(node.left)
                q.append(node.right)
        return ans
    
    def deSerialize(self, arr):
        return buildTree(' '.join(arr)) 
