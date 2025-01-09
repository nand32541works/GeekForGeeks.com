#This is the today's code for solution

class Solution:
    def subarraySum(self, arr, target):
        l=[]
        sum=0
        ind=[]
        for i in range(0,len(arr)):
            l.append(arr[i])
            ind.append(i)
            sum+=arr[i]
            if(sum<target):
                continue
            if(sum==target):
                return([ind[0]+1,ind[-1]+1])
            if(sum>target):
                while(sum>target):
                    ind.pop(0)
                    sum-=l.pop(0)
                    if(sum==target):
                        return([ind[0]+1,ind[-1]+1])
                if(sum==target):
                    return([ind[0]+1,ind[-1]+1])
        return [-1]
