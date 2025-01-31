#This code is written in Python

class Solution: 
    def solveSudoku(self, mat):
        def block_id(r, c):
            return (r//3)*3 + c//3
        def pos(block_id):
            return (block_id//3)*3, (block_id%3)*3
        row_mask = [0]*9
        col_mask = [0]*9
        blk_mask = [0]*9
        for i in range(9):
            mask = 0
            for e in mat[i]:
                if e > 0:
                    mask |= (1<<e)
            row_mask[i] = mask
        for j in range(9):
            mask = 0
            for r in range(9):
                if mat[r][j] > 0:
                    mask |= (1<<mat[r][j])
            col_mask[j] = mask
        for k in range(9):
            mask = 0
            r, c = pos(k)
            for r0 in range(r, r+3):
                for c0 in range(c, c+3):
                    if mat[r0][c0] > 0:
                        mask |= (1<<mat[r0][c0])    
            blk_mask[k] = mask
        def possible_element(r, c):
            m1 = row_mask[r]
            m2 = col_mask[c]
            m3 = blk_mask[block_id(r, c)]
            for n in range(1, 10):
                m = (1<<n)
                if (m&m1 == 0) and (m&m2 == 0) and (m&m3 == 0):
                    yield n
        def place(mat, r, c):
            if r == len(mat):
                return True
            if mat[r][c] == 0:
                for e in possible_element(r, c):
                    mat[r][c] = e
                    row_mask[r] |= (1<<e)
                    col_mask[c] |= (1<<e)
                    blk_mask[block_id(r, c)] |= (1<<e)
                    if place(mat, r+(c+1)//9, (c+1)%9):
                        return True
                    mat[r][c] = 0
                    row_mask[r] ^= (1<<e)
                    col_mask[c] ^= (1<<e)
                    blk_mask[block_id(r, c)] ^= (1<<e)
                else:
                    return False
            else:
                return place(mat, r+(c+1)//9, (c+1)%9)
        place(mat, 0, 0)
        return mat
