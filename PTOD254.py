class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        dq = deque() 
        max_sum = float('-inf')
        for r in range(a, n + 1):
            while dq and dq[0] < r - b:
                dq.popleft()
            l = r - a
            while dq and prefix[dq[-1]] >= prefix[l]:
                dq.pop()
            dq.append(l)
            if dq:
                max_sum = max(max_sum, prefix[r] - prefix[dq[0]])
        return max_sum
