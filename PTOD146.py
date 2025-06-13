class Solution:
    def kokoEat(self,arr,k):
        def ok(s):
            cnt = 0
            for e in arr:
                cnt += e//s + int(e%s != 0)
            return cnt <= k
        lo, hi = 1, 10**6
        while lo < hi:
            mi = lo + (hi-lo)//2
            if ok(mi):
                hi = mi
            else:
                lo = mi+1
        return lo
