from collections import Counter, defaultdict

class Solution:
    def isPossible(self, arr, k):
        freq = Counter(arr)          
        need = defaultdict(int) 
        for num in arr:
            if freq[num] == 0:
                continue  
            if need[num] > 0:
                freq[num] -= 1
                need[num] -= 1
                need[num + 1] += 1  
            elif all(freq[num + i] > 0 for i in range(k)):
                for i in range(k):
                    freq[num + i] -= 1
                need[num + k] += 1  
            else:
                return False  
        return True
