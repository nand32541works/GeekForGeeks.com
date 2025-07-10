class Solution():
    def longestString(self, arr):
        arr.sort(key=len)
        ans = ""
        s = set([""])
        for e in arr:
            if e[:-1] in s:
                if len(e) > len(ans) or len(e) == len(ans) and e < ans:
                    ans = e
                s.add(e)
        return ans
