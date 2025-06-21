class Solution:
    def catchThieves(self, arr, k):
        from collections import deque
        caught_count = 0
        police_q, thief_q = deque(), deque()
        for i, a in enumerate(arr):
            q_a, q_b = (police_q, thief_q) if a == "T" else (thief_q, police_q)
            min_i = i - k
            while q_a and q_a[0] < min_i:
                q_a.popleft()
            if q_a:
                q_a.popleft()
                caught_count += 1
            else:
                q_b.append(i)
        return caught_count
