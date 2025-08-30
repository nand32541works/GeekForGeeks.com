class Solution:
    def celebrity(self, mat):
        # code here
        count = 0
        for item in mat:
            if item.count(1)==1: 
                index = mat.index(item)
                count+=1
                break
        if count==0:
            return -1 
        for item in mat:
            if item[index]==0: 
                return -1
        else:
            return index
