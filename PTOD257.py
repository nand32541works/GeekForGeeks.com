class Solution:
    def possibleWordsRec(self, arr, index, prefix, padMap, res):
        if index == len(arr):
            res.append(prefix)
            return
        digit = arr[index]
        if digit < 2 or digit > 9:
            self.possibleWordsRec(arr, index + 1, prefix, padMap, res)
            return
        for ch in padMap[digit]:
            self.possibleWordsRec(arr, index + 1, prefix + ch, padMap, res)
    def possibleWords(self, arr):
        res = []
        padMap = [
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]
        self.possibleWordsRec(arr, 0, "", padMap, res)
        return res
