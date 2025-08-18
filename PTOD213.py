class Solution:
    def hIndex(self, citations):
        n = len(citations)
        counts = [0] * (n + 1)
        for c in citations:
            counts[min(c, n)] += 1
        count = 0
        for h in reversed(range(n + 1)):
            count += counts[h]
            if count >= h:
                return h
        return 0
