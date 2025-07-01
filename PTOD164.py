class Solution:
    def substrCount(self, s, k):
        from collections import defaultdict
        n, ans = len(s), 0
        cnt = defaultdict(int)
        for i in range(n):
            cnt[s[i]] += 1
            if i >= k:
                cnt[s[i-k]] -= 1
                if cnt[s[i-k]] == 0:
                    cnt.pop(s[i-k])
            if i >= k-1:
                if len(cnt) == k-1:
                    ans += 1
        return ans
