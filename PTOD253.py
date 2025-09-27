class Solution:
    def longestSubarray(self, arr, x):
        from heapq import heappop, heappush
        min_h, max_h = [], []
        max_start = max_end = start = 0
        for end, a in enumerate(arr):
            heappush(min_h, (a, end))
            heappush(max_h, (-a, end))
            while -max_h[0][0] - min_h[0][0] > x:
                h = min_h if min_h[0][1] <= max_h[0][1] else max_h
                if h[0][1] >= start:
                    start = h[0][1] + 1
                heappop(h)
            if end - start > max_end - max_start:
                max_start, max_end = start, end
        return arr[max_start:max_end + 1]
