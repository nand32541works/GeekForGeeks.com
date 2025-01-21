#This is taday's code for PTOD streak

class Solution:
    def reverseKGroup(self, head, k):
        a=[]
        r=0
        t=k
        while head:
            a.append(head.data)
            head=head.next
            t=t-1
            if t==0:
                for i in range(len(a)-1,-1,-1):
                    if r==0:
                        n=Node(a[i])
                        r=n
                    else:
                        n.next=Node(a[i])
                        n=n.next
                t=k
                a=[]
        if t!=0:
            for i in range(len(a)-1,-1,-1):
                    if r==0:
                        n=Node(a[i])
                        r=n
                    else:
                        n.next=Node(a[i])
                        n=n.next
        return r 
