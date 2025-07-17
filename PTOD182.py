class Solution:
    def lcmTriplets(self, n):
        if n<=2:
            return n
        if n%2==0 and n%3==0:
            return (n-1)*(n-2)*(n-3)
        if n%2==0:
            return n*(n-1)*(n-3)
        else:
            return n*(n-1)*(n-2)
