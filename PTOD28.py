#This is the code written in python

import itertools
class Solution:
    def findPermutation(self, s):
        li = {''.join(p) for p in itertools.permutations(s)};
        return list(li)
