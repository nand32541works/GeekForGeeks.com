class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        buckets = [[] for _ in range(n + 1)]
        for i, v in enumerate(arr):
            if v < 0:
                buckets[0].append(i)       
            elif v <= n:
                buckets[v].append(i)      
        parent = list(range(n))
        size = [1] * n
        active = [False] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return ra
        ans = 0
        max_comp = 0
        for x in range(0, n + 1):
            for pos in buckets[x]:
                active[pos] = True
                if pos - 1 >= 0 and active[pos - 1]:
                    union(pos, pos - 1)
                if pos + 1 < n and active[pos + 1]:
                    union(pos, pos + 1)
                root = find(pos)
                if size[root] > max_comp:
                    max_comp = size[root]
            if x >= 1 and max_comp >= x:
                if max_comp > ans:
                    ans = max_comp
        return ans
