class Solution:    
    def minimumPlatform(self,arr,dep):
        from collections import defaultdict
        mp = defaultdict(int)
        for i in range(len(arr)):
            mp[arr[i]] += 1
            mp[dep[i] + 1] -= 1
        max1 = 0
        tong = 0
        for time, change in sorted(mp.items()):
            tong += change
            max1 = max(max1, tong)
        return max1
