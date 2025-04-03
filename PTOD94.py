from collections import deque

class Solution:
    def isSafe(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m
    
    def orangesRotting(self, mat):
        #Code here
        n = len(mat)
        m = len(mat[0])
    
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))
    
        elapsedTime = 0
    
        while q:
            elapsedTime += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dir in directions:
                    x = i + dir[0]
                    y = j + dir[1]
                    if self.isSafe(x, y, n, m) and mat[x][y] == 1:
                        mat[x][y] = 2
                        q.append((x, y))
    
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    return -1
    
        return max(0, elapsedTime - 1)
