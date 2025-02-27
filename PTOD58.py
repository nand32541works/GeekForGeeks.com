#This code is written in python

class Solution:
    def __init__(self):
        self.s = []
        self.minEle = None
    def push(self, x):
        if not self.s:
            self.s.append((x, x))
        else:
            self.s.append((x, min(x, self.s[-1][1])))
    def pop(self):
        if not self.s:
            return
        self.s.pop()
    def peek(self):
        if not self.s:
            return -1
        return self.s[-1][0]
    def getMin(self):
        if not self.s:
            return -1
        return self.s[-1][1]
