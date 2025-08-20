class Solution:
    def searchMatrix(self, mat, x):
        for i in mat:
            if x in i:
                return True
        return False
