from collections import defaultdict
import heapq

class Solution:
    def sumOfModes(self, arr, k):
        freq = defaultdict(int)         
        count_map = defaultdict(set)
        max_freq = 0                    
        result = 0
        for i in range(len(arr)):
            num = arr[i]
            prev_freq = freq[num]
            freq[num] += 1
            new_freq = freq[num]
            if prev_freq > 0:
                count_map[prev_freq].discard(num)
                if not count_map[prev_freq]:
                    del count_map[prev_freq]
            count_map[new_freq].add(num)
            max_freq = max(max_freq, new_freq)
            if i >= k:
                out_num = arr[i - k]
                out_freq = freq[out_num]
                freq[out_num] -= 1
                count_map[out_freq].discard(out_num)
                if not count_map[out_freq]:
                    del count_map[out_freq]
                if freq[out_num] > 0:
                    count_map[freq[out_num]].add(out_num)
                else:
                    del freq[out_num]
                if max_freq not in count_map:
                    max_freq = max(count_map.keys(), default=0)
            if i >= k - 1:
                result += min(count_map[max_freq])
        return result
