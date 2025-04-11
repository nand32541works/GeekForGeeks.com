import heapq
from collections import defaultdict

class Solution:
    def dijkstra(self, V, edges, src):
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  
        dist = [float('inf')] * V
        dist[src] = 0
        min_heap = [(0, src)] 
        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            for neighbor, weight in adj[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        return dist
