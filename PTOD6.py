#This is code in python

import math
class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        res=[]
        i=0
        td = float('inf')
        j=len(arr)-1
        while(i<j):
            sump=arr[i]+arr[j]
            d=abs(target-sump)
            if d <td:
                res=[0,0]
                td =d
                res[0]=arr[i]
                res[1]=arr[j]
            if sump < target:
                i += 1
            elif sump > target:
                j -= 1
            else:
                break
        return res
