class Solution:
    def minCost(self, n, m, x, y):
        x.sort()
        y.sort()
        hCount, vCount = 1, 1
        i, j = len(x) - 1, len(y) - 1
        totalCost = 0
        while i >= 0 and j >= 0:
            if x[i] >= y[j]:
                totalCost += x[i] * hCount
                vCount += 1
                i -= 1
            else:
                totalCost += y[j] * vCount
                hCount += 1
                j -= 1
        while i >= 0:
            totalCost += x[i] * hCount
            vCount += 1
            i -= 1
        while j >= 0:
            totalCost += y[j] * vCount
            hCount += 1
            j -= 1

        return totalCost
