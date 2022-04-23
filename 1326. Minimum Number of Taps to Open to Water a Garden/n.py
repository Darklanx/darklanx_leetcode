
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach = defaultdict(lambda: 0)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = max(0, i-r)
            right = i+r
            reach[left] = max(reach[left], right)
            

        cur_reach = reach[0]
        next_reach = cur_reach
        count = 1
        if cur_reach >= n:
            return count
    
        for i in range(1, n+1):
            if i > cur_reach:
                return -1
            
            next_reach = max(next_reach, reach[i])
            if next_reach >= n:
                return count + 1
            
            if i == cur_reach:
                count += 1
                cur_reach = next_reach
            
        return count
            