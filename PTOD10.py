#This is a Python code

class Solution:
    def countDistinct(self, a, k):
        r=[]
        for i in range(len(a)-k+1):
            l=a[i:i+k]
            le=len(set(l))
            r.append(le)
        return r
