class Solution:
    def insertInterval(self, intervals, newInterval):
        from bisect import bisect_left, bisect_right
        new_start, new_end = newInterval
        last_end = intervals[-1][1]
        start_i = bisect_left(intervals, [new_start, 0])
        end_i = bisect_right(intervals, [new_end, last_end], lo=start_i)
        
        if start_i > 0 and new_start <= intervals[start_i - 1][1]:
            start_i -= 1
            new_start = intervals[start_i][0]
        if end_i > 0 and intervals[end_i - 1][1] > new_end:
            new_end = intervals[end_i - 1][1]
        if start_i == end_i:
            intervals.insert(start_i, newInterval)
        else:
            intervals[start_i:end_i] = [[new_start, new_end]]
        return intervals
