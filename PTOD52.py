#This code is written in python

class Solution:
    def isBalanced(self, s):
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching:
                if not stack:
                    return False
                if stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)
        return not stack
