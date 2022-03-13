#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# 3 2 5 4 1 0 0
#     6 6 5 5 6
# 7
# 0
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        l = len(nums)
        nums[-1] = l-1 # last index
        for i in reversed(range(l)):
            # max look forward, l-i to avoid invalid index)
            step = nums[i]
            nums[i] = i
            for j in range(1, min(step + 1, l-i)):
                nums[i] = max(nums[i], nums[i + j])
                if nums[i] >= l-1:
                    break
        print(nums)
        return nums[0] >= l-1
        
# 2 3 1 1 4
#         4
# @lc code=end

