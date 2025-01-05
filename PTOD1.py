#Please code you can copy:

class Solution:
    def anagrams(self, arr):
        mpp = {}
        res = []
        for word in arr:
            key = "".join(sorted(word))
            if key not in mpp:
                mpp[key] = []
            mpp[key].append(word)
        for key in mpp.keys():
            aux = mpp[key]
            res.append(aux)
        return res
