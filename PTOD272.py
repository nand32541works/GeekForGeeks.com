class Solution:
    def countNodes(self, root):
        curr = root
        nodes = 0
        while curr:
            if curr.left is None:
                nodes += 1
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
                    nodes += 1
        return nodes
    def findMedian(self, root):
        n = self.countNodes(root)
        if n % 2 == 0:
            medianIndex = n // 2
        else:
            medianIndex = (n + 1) // 2
        curr = root
        nodes = 0
        while curr:
            if curr.left is None:
                nodes += 1
                if nodes == medianIndex:
                    return curr.data
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    nodes += 1
                    if nodes == medianIndex:
                        return curr.data
                    prev.right = None
                    curr = curr.right
        return -1
