class Solution:
    def swapKth(self, head, k):
        if not head:
            return head
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        if k > n:
            return head
        if 2 * k - 1 == n:
            return head
        prevX = None
        x = head
        for i in range(1, k):
            prevX = x
            x = x.next
        prevY = None
        y = head
        for i in range(1, n - k + 1):
            prevY = y
            y = y.next
        if prevX:
            prevX.next = y
        if prevY:
            prevY.next = x
        tempNext = x.next
        x.next = y.next
        y.next = tempNext
        if k == 1:
            head = y
        if k == n:
            head = x
        return head
