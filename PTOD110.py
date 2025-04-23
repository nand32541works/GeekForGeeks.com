from collections import Counter

class Solution:
	def singleNum(self, arr):
		count = Counter(arr)
        return sorted([item for item in arr if count[item] == 1])
