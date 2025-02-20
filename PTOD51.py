#This code is written in python

import heapq
class Solution:
    def getMedian(self, arr):
        max_heap = [] 
        min_heap = []  
        medians = []
        for number in arr:
            if not max_heap or number <= -max_heap[0]:
                heapq.heappush(max_heap, -number)
            else:
                heapq.heappush(min_heap, number)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            if len(max_heap) > len(min_heap):
                median = float(-max_heap[0])
            else:
                median = (-max_heap[0] + min_heap[0]) / 2.0
            medians.append(median)
        return medians
