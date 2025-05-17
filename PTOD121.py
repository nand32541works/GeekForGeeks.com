class Solution:
	def sortArray(self, arr, A, B, C):
		return sorted(list(map(lambda x : A*(x**2) + B*(x) + C, arr)))
