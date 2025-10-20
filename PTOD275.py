class Solution:
    def topKFreq(self, arr, k):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        maxFreq = max(freq.values())
        buckets = [[] for _ in range(maxFreq + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        
        for i in range(maxFreq, 0, -1):
            buckets[i].sort(reverse=True)
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
