class Solution:
    def findUnique(self, arr):
        from functools import reduce
        from operator import xor
        return reduce(xor, arr)
