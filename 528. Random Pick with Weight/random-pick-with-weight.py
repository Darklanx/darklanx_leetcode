import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        
        
    def pickIndex(self) -> int:
        prob = random.random()
        return bisect.bisect_left(self.prefix_sums, prob * self.total_sum)
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()