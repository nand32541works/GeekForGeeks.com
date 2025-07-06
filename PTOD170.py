class Solution:
    def topKSumPairs(self, a, b, k):
        from heapq import heapify, heappop, heappush
        n = len(a)
        for i in range(n):
            a[i] *= -1
            b[i] *= -1
        a.sort()
        b.sort()
        h = [(a[i] + b[0], i, 0) for i in range(n)]
        heapify(h)
        output = []
        while len(output) < k:
            min_sum, i, j = heappop(h)
            output.append(-min_sum)
            if j < n - 1:
                heappush(h, (a[i] + b[j + 1], i, j + 1))
        return output
