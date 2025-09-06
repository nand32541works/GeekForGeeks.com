class Solution:
    def lengthOfLoop(self, head):
        slow, fast = head, head.next
        while fast and fast.next and fast != slow:
            slow, fast = slow.next, fast.next.next
        if slow != fast:
            return 0
        length, slow = 1, slow.next
        while slow != fast:
            length += 1
            slow = slow.next
        return length
