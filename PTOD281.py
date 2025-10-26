class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        import heapq
        if not arr1 or not arr2:
            return []
        min_heap = []
        result = []
        for j in range(min(k, len(arr2))):
            heapq.heappush(min_heap, (arr1[0] + arr2[j], 0, j))
    
        while min_heap and len(result) < k:
            s, i, j = heapq.heappop(min_heap)
            result.append([arr1[i], arr2[j]])
            if i + 1 < len(arr1):
                heapq.heappush(min_heap, (arr1[i + 1] + arr2[j], i + 1, j))
        return result
