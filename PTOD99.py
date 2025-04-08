from collections import defaultdict

class Solution:
    def isBridge(self, V, edges, c, d):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        visited = set()
        dfs(c, visited)
        before_removal = len(visited)
        if d in graph[c]:
            graph[c].remove(d)
        if c in graph[d]:
            graph[d].remove(c)
        visited = set()
        dfs(c, visited)
        after_removal = len(visited)
        return before_removal != after_removal
