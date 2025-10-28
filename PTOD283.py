from collections import deque, defaultdict
class Solution:
    def diameter(self, V, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(start):
            visited = [-1] * V
            q = deque([start])
            visited[start] = 0
            farthest_node = start
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if visited[nei] == -1:
                        visited[nei] = visited[node] + 1
                        q.append(nei)
                        if visited[nei] > visited[farthest_node]:
                            farthest_node = nei
            return farthest_node, visited[farthest_node]
        visited_global = [False] * V
        diameter = 0
        for i in range(V):
            if not visited_global[i]:
                far1, _ = bfs(i)
                far2, dist = bfs(far1)
                def mark_component(node):
                    q = deque([node])
                    while q:
                        curr = q.popleft()
                        if visited_global[curr]:
                            continue
                        visited_global[curr] = True
                        for nei in graph[curr]:
                            if not visited_global[nei]:
                                q.append(nei)
                mark_component(i)
                diameter = max(diameter, dist)
        return diameter
