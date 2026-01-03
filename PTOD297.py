class Solution:
    def flatten(self, root):
        cur=root
        arr=[]
        while cur:
            down=cur
            while down:
                arr.append(down.data)
                down=down.bottom
            cur=cur.next
        arr.sort()
        head=Node(0)
        cur=head

        for i in arr:
            cur.bottom=Node(i)
            cur=cur.bottom
        return head.bottom
