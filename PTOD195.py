class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict
        count_map = defaultdict(int)
        for start, end in intervals:
            count_map[start] += 1
            count_map[end + 1] -= 1 
        sorted_points = sorted(count_map.keys())
        current_count = 0
        max_powerful = -1
        for i in range(len(sorted_points) - 1):
            point = sorted_points[i]
            current_count += count_map[point]
            if current_count >= k:
                next_point = sorted_points[i + 1]
                max_powerful = max(max_powerful, next_point - 1)
                
        return max_powerful
