class Solution:
    def activitySelection(self, start, finish):
        activities = sorted(zip(finish, start))
        count, last_end = 0, -1
        for end, begin in activities:
            if begin > last_end:
                count += 1
                last_end = end
        return count
