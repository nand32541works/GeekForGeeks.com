class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = [(deadline[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: -x[1])
        parent = [i for i in range(max(deadline) + 1)]
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            parent[u] = v
        count, total_profit = 0, 0
        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                count += 1
                total_profit += p
                union(available_slot, available_slot - 1)
        return count, total_profit
