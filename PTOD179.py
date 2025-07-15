class Solution:
    def divby13(self, s):
        v = 0
        for x in s:
            v = v*10 + (ord(x) - ord('0'))
            if v%13 == 0:
                v = 0
        return v == 0
