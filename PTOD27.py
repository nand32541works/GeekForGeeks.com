#this code is in python

class LRUCache: 
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.order = []
        
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
        
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.cap:
            lru = self.order.pop(0)
            del self.cache[lru]
        self.cache[key] = value
        self.order.append(key)
