#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        MAX_CHAR = 26
        n = len(s)
        res = 0
        lastIndex = [-1] * MAX_CHAR
        start = 0
        for end in range(n):
            start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)
            res = max(res, end - start + 1)
            lastIndex[ord(s[end]) - ord('a')] = end
        return res
