class Solution:  
    def findMaxSum(self,arr):
        stolen, notstolen, n = 0, 0, len(arr)
        for i in range(n):
            n_stolen = max(stolen, notstolen+arr[i]) 
            n_notstolen = max(stolen, notstolen)
            stolen, notstolen = n_stolen, n_notstolen
        return max(stolen, notstolen)
