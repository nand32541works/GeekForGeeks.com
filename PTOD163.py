class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        def is_possible(min_height):
            available_days = k
            curr_growth = 0
            change = [0] * (n + w)
            for i, h in enumerate(arr):
                curr_growth += change[i]
                h += curr_growth
                if h >= min_height:
                    continue
                needed_days = min_height - h
                if needed_days > available_days:
                    return False
                available_days -= needed_days
                curr_growth += needed_days
                change[i + w] -= needed_days
            return True
        lo, hi = min(arr), max(arr) + k
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
