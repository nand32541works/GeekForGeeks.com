class Solution:
    def findSpiral(self, root):
        level = 0
        q = [root]
        ans = []
        while q:
            nq = []
            n = len(q)
            for i in range(n):
                if q[i].left:
                    nq.append(q[i].left)
                if q[i].right:
                    nq.append(q[i].right)
                if level&1 != 0:
                    ans.append(q[i].data)
                else:
                    ans.append(q[n-1-i].data)
            q = nq
            level += 1
        return ans
