class Solution:
    def findOrder(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        inDegree = [0] * n
        for dest, src in prerequisites:
            adj[src].append(dest)
            inDegree[dest] += 1
        q = deque([i for i in range(n) if inDegree[i] == 0])
        order = []
        
        while q:
            current = q.popleft()
            order.append(current)
            for neighbor in adj[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)
        if len(order) == n:
            return order
        return []
