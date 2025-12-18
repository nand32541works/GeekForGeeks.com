class Solution:
    def sortIt(self, arr):
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                arr[i] *= -1
        arr.sort()
        
        for i in range(len(arr)):
            if arr[i] < 0:
                arr[i] *= -1
