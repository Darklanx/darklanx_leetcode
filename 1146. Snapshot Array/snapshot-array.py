'''
Naive idea is to literally create snapshot of all lists
However for every snapshot, there could be only some difference.
(0, 5) (0, 0) (0, 0)
(1, 6)
       (2, 6)

0, 1
0
'''
from dataclasses import dataclass
class SnapshotArray:
    # Data = namedtuple('Data', ['version', 'val'])
    @dataclass
    class Data:
        version: int
        val: int = 0
    
    def __init__(self, length: int):
        self.n_snap = 0
        self.records = defaultdict(list)
        for i in range(length):
            self.records[i].append(SnapshotArray.Data(self.n_snap, 0))

    def set(self, index: int, val: int) -> None:
        target_record = self.records[index]
        if self.n_snap == target_record[-1].version:
            target_record[-1].val = val
        else:
            target_record.append(SnapshotArray.Data(self.n_snap, val))
            
        
    def snap(self) -> int:
        self.n_snap += 1
        return self.n_snap - 1 
        

    def get(self, index: int, snap_id: int) -> int:
        record = self.records[index]
        l = 0
        r = len(record)
        while l < r:
            mid = l + (r - l)//2
            if record[mid].version <= snap_id:
                l = mid + 1
            else:
                r = mid
                
        return record[l-1].val
            
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)