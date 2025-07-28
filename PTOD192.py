class Solution:
     def balanceSums(self, mat):
        max_sum = max(max(map(sum, mat)), max(map(sum, zip(*mat))))
        return max_sum * len(mat) - sum(map(sum, mat))
