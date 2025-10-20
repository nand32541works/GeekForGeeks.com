from math import comb

class Solution:
    def countBSTs(self, arr):
        def num_bsts(n):
            return comb(2 * n, n) // (n + 1)
        arr_sorted = sorted(arr)
        n = len(arr)
        catalan = [num_bsts(i) for i in range(n + 1)]
        result = []
        for x in arr:
            idx = arr_sorted.index(x)
            left = idx              
            right = n - idx - 1     
            result.append(catalan[left] * catalan[right])
        return result
