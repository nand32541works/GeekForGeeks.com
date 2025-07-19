class Solution:
    def countValid(self, n, arr):
        m, z = len(arr), 0 in arr
        return 9*10**(n-1) - (9-m+z)*(10-m)**(n-1)
