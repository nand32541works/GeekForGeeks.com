class Solution:
    def farMin(self, arr):
        n = len(arr)
        indices = sorted(list(range(n)), key=lambda i: arr[i])
        largest_index = indices[0] 
        ans = [0]*n
        
        for i in indices:
            if largest_index > i: 
                ans[i] = largest_index
            else: 
                ans[i] = -1
            largest_index = max(largest_index, i)
        return ans
