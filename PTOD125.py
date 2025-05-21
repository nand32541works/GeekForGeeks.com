class Solution(object):
    def kthSmallest(self, m, n, k):
        def oye(a):
            c = 0
            for i in range(1,m+1):
                c += min(a//i,n)
            return c
        s = 1
        e = m * n
        while s < e:
            mi = s + (e - s)//2
            if oye(mi) < k:
                s = mi + 1
            else: 
                e = mi 
        return s
