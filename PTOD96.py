class Solution:
    def numIslands(self, grid):
        def dfs(i,j):
            ctr=0
            for rr,cc in [[0,1],[-1,0],[1,0],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]:
                nr,nc=i+rr,j+cc
                if 0<=nr<r and 0<=nc<c and grid[nr][nc]=='L':
                    grid[nr][nc]=0
                    dfs(nr,nc)
            return
            
        r,c=len(grid),len(grid[0])
        total=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='L':
                    grid[i][j]=0
                    dfs(i,j)
                    total+=1
        return total
