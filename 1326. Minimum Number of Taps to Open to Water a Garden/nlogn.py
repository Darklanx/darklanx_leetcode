
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [[i-r, i+r] for i, r in enumerate(ranges) if r > 0]
        cur_reach = 0 # how far we can currently water
        next_reach = 0 # how far we can water after we add out best candidate
        count = 0
        taps.sort()
        for i, tap in enumerate(taps):
            l, r = tap
            if l > cur_reach: # if the new tap is out of reach, we must now include of best candidate to increase our reaach
                cur_reach = next_reach
                count += 1
                
            if l > cur_reach: # if the current tap is out of reach, then some area between cur_reach and l cannot be watered
                return -1
            next_reach = max(next_reach, r)

            if next_reach >= n:
                return count + 1
        
        return -1