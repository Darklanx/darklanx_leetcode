import enum

class Type(enum.Enum):
    START = 0
    PERSON = 1
    END = 2

class TimeData:
    def __init__(self, t, _type, p_idx=None):
        self.t = t
        self.type = _type
        self.p_idx = p_idx
    
    def __lt__(self, other):
        return self.t < other.t if self.t != other.t else self.type.value < other.type.value

    
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        timestamps = []
        for fl in flowers:
            start, end = fl
            td_start = TimeData(start, Type.START)
            td_end = TimeData(end, Type.END)
            
            timestamps.append(td_start)
            timestamps.append(td_end)
        
        for i, p in enumerate(persons):
            td = TimeData(p, Type.PERSON, i)
            timestamps.append(td)
            
        timestamps.sort()
        ans = [0 for i in range(len(persons))]
        count = 0
        for td in timestamps:
            if td.type == Type.PERSON:
                ans[td.p_idx] = count
            elif td.type == Type.START:
                count += 1
            else: # Type.END
                count -= 1
                
            
        return ans