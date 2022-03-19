'''
11 => 0
101 => 1
1001 => 1
10001 => 2
100001 => 2
100 0 001 => 3
1000 0001 => 3
(empty space + 1) //2
Careful edge case

1. 1000101
2. 00010
3. 01000

'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 1
        prev_dude = None
        for idx, seated in enumerate(seats):
            if seated:
                if prev_dude is not None:
                    continguous_spaces = idx - prev_dude - 1  
                    max_dist = max(max_dist, (continguous_spaces + 1) // 2)
                else:
                    max_dist = max(max_dist, idx)
                
                prev_dude = idx
                
        max_dist = max(max_dist, len(seats) - 1 - prev_dude)
                
            
        return max_dist
            
        