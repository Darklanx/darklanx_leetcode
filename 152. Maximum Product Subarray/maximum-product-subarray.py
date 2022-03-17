'''
# 1. assume no 0
[2,3,-2,4]
[(2,2) (6, 3), (-2, -12), (4, -48)]

[-2, 0, -1]
[(-2, -2), (0, 0), (-1, -1)]

[-1]
# 2. with 0
'''
from collections import namedtuple
import math
from typing import List
MaxMin = namedtuple("MaxMin", ['max', 'min'])
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_min = [MaxMin(1, 1)]
        max_prod = -math.inf
        max_min = MaxMin(1, 1)
        for num in nums:
            _max = max(num, num * max_min.max, num * max_min.min)
            _min = min(num, num * max_min.max, num * max_min.min)
            max_min = MaxMin(_max, _min)
            max_prod = max(_max, max_prod)
            
        return max_prod
            