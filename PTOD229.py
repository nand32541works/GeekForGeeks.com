class Solution:
    def reverse(self, head):
        while head.next:
            head.prev, head.next, head = head.next, head.prev, head.next
        head.next, head.prev = head.prev, None
        return head
