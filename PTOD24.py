#THIS CODE IS WRITTEN IN PYTHON for taday's PTOD streak

class Solution:
    def detectLoop(self, head):
        #code here
        s, f = head, head.next
        while f and f.next:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        return False
