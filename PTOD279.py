import heapq
class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        half = total / 2.0
        pq = [-float(x) for x in arr]
        heapq.heapify(pq)
        ans = 0
        while total > half:
            top = -heapq.heappop(pq)
            total -= top / 2.0
            heapq.heappush(pq, -(top / 2.0))
            ans += 1
        return ans
