#This code is written in Python

class Solution:
    def longestSubarray(self, arr, k):  
        pre={0:-1}
        s=0
        mx=0
        n=len(arr)
        for i in range(n):
            s+=arr[i]
            if s-k in pre:mx=max(mx,i-pre[s-k])
            if s not in pre:
                pre[s]=i
        return mx
