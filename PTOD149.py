class Solution:
    def minCost(self, heights, cost):
        def compute_cost(h):
            r = 0
            for i in range(len(heights)):
                r += cost[i] * abs(heights[i] - h)
            return r
        lo, hi = min(heights), max(heights)
        while hi - lo > 2:
            m1 = lo + (hi-lo)//3
            m2 = hi - (hi-lo)//3
            c1, c2 = compute_cost(m1), compute_cost(m2)
            if c1 > c2:
                lo = m1
            else:
                hi = m2
        return min(compute_cost(h) for h in range(lo, hi + 1))
