class Solution:
    def minDeletions(self,s):
        # code here 
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                st = j
                ed = j + i
                diff = 0 if s[st] == s[ed] else 2
                dp[st][ed] = min(dp[st+1][ed-1] + diff, 1 + dp[st+1][ed], 1 + dp[st][ed-1])
        return dp[0][-1]
