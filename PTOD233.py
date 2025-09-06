from queue import PriorityQueue
class Solution:
    def mergeKLists(self, arr):
        pq = PriorityQueue()
        for head in arr:
            while head:
                pq.put(head.data)
                head = head.next
        tail = head = None
        while pq.qsize():
            if not head:
                head = tail = Node(pq.get())
                continue
            tail.next = Node(pq.get())
            tail = tail.next
        return head 
