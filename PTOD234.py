'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        def merge(l, r):
            ret = w = Node(0)
            while l and r:
                if l.data < r.data:
                    w.next = l
                    l = l.next
                else:
                    w.next = r
                    r = r.next
                w = w.next
                w.next = None
            while l:
                w.next = l
                l = l.next
                w = w.next
            while r:
                w.next = r
                r = r.next
                w = w.next
            return ret.next
        def merge_sort(h, n):
            if n <= 1:
                return h
            n1 = n//2
            n2 = n - n1
            t = h
            for _ in range(1, n1):
                t = t.next
            h2 = t.next
            t.next = None
            lh = merge_sort(h, n1)
            rh = merge_sort(h2, n2)
            return merge(lh, rh)
        n = 0
        t = head
        while t:
            n += 1
            t = t.next
        return merge_sort(head, n)
