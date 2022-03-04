#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        min_idx = l-1 # track the smallest pos that can reach the last index
        for i in reversed(range(l)):
            if i + nums[i] >= min_idx:
                min_idx = i

        return min_idx == 0
# @lc code=end

