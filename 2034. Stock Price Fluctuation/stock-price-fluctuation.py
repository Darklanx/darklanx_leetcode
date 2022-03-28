import heapq
from collections import namedtuple
from dataclasses import dataclass
Record = namedtuple("Record", ['price', 'timestamp', 'version'])


class StockPrice:
    

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.records = {}
        self._current = Record(-math.inf, -math.inf, -math.inf)

    def update(self, timestamp: int, price: int) -> None:
        version = 0 if timestamp not in self.records else self.records[timestamp].version + 1
        rec = Record(price, timestamp, version)
        self.records[timestamp] = rec
        
        if timestamp >= self._current.timestamp:
            self._current = rec
        
        heapq.heappush(self.max_heap, Record(price * -1, timestamp, version))
        heapq.heappush(self.min_heap, Record(price, timestamp, version))
        
    def current(self) -> int:
        return self._current.price
        

    def maximum(self) -> int:
        top = self.max_heap[0]
        while self.records[top.timestamp].version != top.version:
            heapq.heappop(self.max_heap)
            top = self.max_heap[0]
        return self.max_heap[0].price * -1
        

    def minimum(self) -> int:
        top = self.min_heap[0]
        while self.records[top.timestamp].version != top.version:
            heapq.heappop(self.min_heap)
            top = self.min_heap[0]
        return self.min_heap[0].price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()