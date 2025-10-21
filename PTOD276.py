import heapq as h
class Solution:
    def nearlySorted(self, arr, k):
        a=[]
        j=0
        for i in range(len(arr)):
            h.heappush(a,arr[i])
            if len(a)>k:
                arr[j]=h.heappop(a)
                j+=1
        while len(a)>0:
            arr[j]=h.heappop(a)
            j+=1
        return arr
