class Solution:
    def longestStringChain(self, words):
        ans = 0
        sorted_strings = sorted(words, key=len) 
        dp = {}  
        for word in sorted_strings:  
            dp[word] = 1  
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:] 
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)  
            ans = max(ans, dp[word])  
        return ans
