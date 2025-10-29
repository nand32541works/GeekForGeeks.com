from collections import deque
class Solution:
    def fill(self, mat):
        rows, cols = len(mat), len(mat[0])
        visited = set()
        queue = deque()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            r, c = queue.popleft()
            mat[r][c] = 'T'  
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 'O' and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 'O':
                    mat[r][c] = 'X'
                elif mat[r][c] == 'T':
                    mat[r][c] = 'O'
        return mat
