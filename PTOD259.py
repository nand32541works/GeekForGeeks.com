class Solution:
    direction = "DLRU"
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    def isValid(self, row, col, n, maze):
        return 0 <= row < n and 0 <= col < n and maze[row][col] == 1
    def findPath(self, row, col, maze, n, ans, currentPath):
        if row == n - 1 and col == n - 1:
            ans.append(currentPath)
            return
        maze[row][col] = 0
        for i in range(4):
            nextRow = row + self.dr[i]
            nextCol = col + self.dc[i]
            if self.isValid(nextRow, nextCol, n, maze):
                currentPath += self.direction[i]
                self.findPath(nextRow, nextCol, maze, n, ans, currentPath)
                currentPath = currentPath[:-1]
        maze[row][col] = 1

    def ratInMaze(self, maze):
        result = []
        n = len(maze)
        currentPath = ""
        if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
            self.findPath(0, 0, maze, n, result, currentPath)
        result.sort()
        return result
