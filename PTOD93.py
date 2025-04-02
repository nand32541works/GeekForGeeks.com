from collections import deque
class Solution:
    def bfs(self, adj):
        ans = []
        vis = set()
        q = deque()
        q.append(0)
        while q:
            c = q.popleft()
            if c in vis:
                continue
            vis.add(c)
            ans.append(c)
            for v in adj[c]:
                q.append(v)
        return ans
