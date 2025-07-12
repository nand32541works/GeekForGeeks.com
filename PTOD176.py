class Solution:
    def maxGold(self, mat):
        n = len(mat)
        m = len(mat[0])
        for y in range(m - 2, -1, -1):
            for x in range(n):
                max_prev = 0
                if x - 1 >= 0:
                    max_prev = max(max_prev, mat[x - 1][y + 1])
                max_prev = max(max_prev, mat[x][y + 1])
                if x + 1 < n:
                    max_prev = max(max_prev, mat[x + 1][y + 1])
                mat[x][y] += max_prev
        return max(mat[i][0] for i in range(n))
