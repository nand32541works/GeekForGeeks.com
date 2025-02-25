#This code is in python

class Solution:
    def getMaxArea(self,arr):
        left = []
        st = []
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                left.append(0)
            else:
                left.append(st[-1]+1)
            st.append(i)
        st = []
        right = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                right[i] = len(arr)-1
            else:
                right[i] = st[-1]-1
            st.append(i)
        res = 0
        for i in range(len(arr)):
            res = max(res,arr[i]*(right[i]-left[i]+1))
        return res
