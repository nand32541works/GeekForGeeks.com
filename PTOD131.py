class Solution:
	def leafNodes(self, preorder):
		ans = []
		def collect(arr):
		    nonlocal ans
		    if not arr:
		        return
		    if len(arr) == 1:
		        ans.append(arr[0])
	        collect([x for x in arr if x < arr[0]])
	        collect([x for x in arr if x > arr[0]])
        collect(preorder)
        return ans
