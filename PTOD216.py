class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        def canPlace(mid):
            count, last = 1, arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]
                if count >= k:
                    return True
            return False
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid
                low = mid + 1   
            else:
                high = mid - 1  
        return ans
