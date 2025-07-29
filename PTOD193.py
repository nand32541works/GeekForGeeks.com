class Solution:
    def asciirange(self, s):
        mp = {}
        prefix_sum = []
        sm = 0
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = [i]
            else:
                mp[s[i]].append(i)
            sm += ord(s[i])
            prefix_sum.append(sm)
        result = []
        alpha = []
        for k,v in mp.items():
            if len(v)>=2:
                alpha.append(k)
        for i in range(len(alpha)):
            fst_idx = mp[alpha[i]][0]
            lst_idx = mp[alpha[i]][-1]-1
            if fst_idx!=lst_idx:
                diff = prefix_sum[lst_idx]-prefix_sum[fst_idx]
                result.append(diff)
        return result
