class Solution:
     def count(self, coins, Sum):
        dp = [0] * (Sum + 1)
        dp[0] = 1
        for coin in coins:
            for sub_sum in range(coin, Sum + 1):
                dp[sub_sum] += dp[sub_sum - coin]
        return dp[-1]
