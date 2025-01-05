#Code you can copy

class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        left, right = 0, len(arr) - 1
        pairs = 0
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum < target:
                pairs += right - left
                left = left + 1
            else:
                right = right - 1
        return pairs
