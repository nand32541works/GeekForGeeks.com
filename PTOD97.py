class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        def dfs(node, visited, stack):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack)
            stack.append(node)

        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)

        return stack[::-1]
