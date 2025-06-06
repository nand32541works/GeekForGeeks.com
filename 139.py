class Solution:
    def search(self, pat, txt):
        n = len(txt)
        list = [];
        start = 0
        end = len(txt)
        while(n > 0):
            try:
                index = txt.index(pat,start,end)
            except:
                break
            list.append(index+1)
            start = index+1
            n -= 1
        return list
