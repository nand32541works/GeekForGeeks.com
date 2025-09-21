class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        res = [0] * n
        windowMax = [0] * (n + 1)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                wsize = right - left - 1
                windowMax[wsize] = \
                    max(windowMax[wsize], arr[top])
            stack.append(i)
            
        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1
            right = n
            wsize = right - left - 1
            windowMax[wsize] = \
                max(windowMax[wsize], arr[top])
        for i in range(n):
            res[i] = windowMax[i + 1]
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i], res[i + 1])
        return res
