#This code is written in python

class Solution:
    def calculateSpan(self, a):
        def traverse():
            b,c=[],[]
            for i in range(len(a)):
                if len(b)==0:
                    c.append(i+1)
                    b.append(i)
                elif a[b[-1]]<=a[i]:
                    while(len(b)!=0 and a[b[-1]]<=a[i]):
                        b.pop()
                    if len(b)==0:
                        c.append(i+1)
                        b.append(i)
                    else:
                        c.append(i-b[-1])
                        b.append(i)
                else:
                    c.append(i-b[-1])
                    b.append(i)
            return c
        c=traverse()
        return c
