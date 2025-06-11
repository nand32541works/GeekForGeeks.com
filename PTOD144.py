class Solution:
    def findLength(self, color, radius):
        stk=[]
        for c,r in zip(color,radius):
            if stk and stk[-1]==(c,r,):
                stk.pop()
                continue
            stk.append((c,r,))
        return len(stk)
