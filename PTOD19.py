#This is the today's solution for GFG

class Solution:
    def rotate(self, head, k):
        cur = head
        last = head
        len = 0
        while cur:
            last = cur
            cur = cur.next
            len += 1
        k = k % len
        if k == 0 or len == 1 or len == k:
            return head
        cur = head
        while k > 1:
            cur = cur.next
            k -= 1
        ans = cur.next
        cur.next = None
        last.next = head
        return ans
