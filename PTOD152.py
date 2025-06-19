class Solution:
    def caseSort(self,s):
        counts = [0] * (ord("z") + 1)
        for c in s:
            counts[ord(c)] += 1
        output = []
        l, u = ord("a"), ord("A")
        for c in s:
            if c < "a":
                while counts[u] == 0:
                    u += 1
                counts[u] -= 1
                output.append(chr(u))
            else:
                while counts[l] == 0:
                    l += 1
                counts[l] -= 1
                output.append(chr(l))
        return "".join(output)
