from collections import deque
class Solution:
    def shortCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = float('inf')
        for i in range(V):
            dist = [-1] * V
            par = [-1] * V
            q = deque()
            q.append(i)
            dist[i] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        par[v] = u
                        q.append(v)
                    elif par[u] != v:
                        ans = min(ans, dist[u] + dist[v] + 1)
        return -1 if ans == float('inf') else ans
