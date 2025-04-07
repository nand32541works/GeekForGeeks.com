class Solution:
    def isCycle(self, V, edges):
        in_degree = [0] * V
        graph = [[] for _ in range(V)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
        for node_list in graph:
            for node in node_list:
                in_degree[node] += 1
        queue = []
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        sorted_nodes = []
        while queue:
            current = queue.pop(0)
            sorted_nodes.append(current)
            for adjacent in graph[current]:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    queue.append(adjacent)
        return len(sorted_nodes) < V
