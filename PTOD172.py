from collections import defaultdict
class Solution:
    def findGreater(self, arr):
        ans = [0 for _ in range(len(arr))]
        hm = defaultdict(int)
        for i in range(len(arr)):
            hm[arr[i]] += 1
        stack = [[arr[-1], hm[arr[-1]]]]
        for i in range(len(arr)-2, -1, -1):
            while stack and stack[-1][1] <= hm[arr[i]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][0]
            else:
                ans[i] = -1
            stack.append([arr[i], hm[arr[i]]])
        ans[-1] = -1
        return ans
