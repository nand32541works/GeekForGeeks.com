class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        if len(prices)/(k+1) == len(prices)//(k+1):
            buy=len(prices)//(k+1)
        else:
            buy=(len(prices)//(k+1))+1
        mini=sum(prices[:buy])
        maxi=sum(prices[-buy:])
        return [mini, maxi]
