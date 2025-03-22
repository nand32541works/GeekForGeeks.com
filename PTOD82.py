class Solution:
    def maxValue(self, arr):
        lth=len(arr)
        dp=[0,0]+arr[1:]
        for ix in range(2,lth+1):
            dp[ix%3]=max(dp[(ix-1)%3],dp[(ix-2)%3]+arr[ix-1])
        mx=max(dp)
        dp=[0,0]+arr[:-1]
        for ix in range(2,lth+1):
            dp[ix%3]=max(dp[(ix-1)%3],dp[(ix-2)%3]+arr[ix-2])
        return max(mx,*dp)
