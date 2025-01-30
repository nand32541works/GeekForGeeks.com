#This code is written in python

class Solution:
    def nQueen(self, n):
        board=[[0 for _ in range(n)] for _ in range(n)]
        res=[]
        self.rec(board,0,0,n,res)
        return res
    def rec(self,board,nq,col,n,res):
        if col>=n:
            if nq>=n:
                tmp=[]
                for j in range(n):
                    for i in range(n):
                        if board[i][j]==1:
                            tmp.append(i+1)
                res.append(tmp)
            return
        for i in range(n):
            if self.canPlace(board,i,col,n):
                board[i][col]=1
                self.rec(board,nq+1,col+1,n,res)
                board[i][col]=0
    def canPlace(self,board,r,c,n):
        for j in range(c):
            if board[r][j]==1:
                return False
        for i in range(r):
            if board[i][c]==1:
                return False
        i,j=r,c
        while i>=0 and j>=0:
            if board[i][j]==1:
                return False
            i-=1
            j-=1
        i,j=r,c
        while i<n and j>=0:
            if board[i][j]==1:
                return False
            i+=1
            j-=1
        return True
