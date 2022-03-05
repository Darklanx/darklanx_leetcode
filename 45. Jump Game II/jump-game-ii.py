from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        last_idx = len(nums) - 1
        cur = 0
        farthest = cur + nums[cur]
        steps = 0
        while cur < last_idx:
            if cur + nums[cur] >= last_idx:
                return steps+1
            for i in range(cur+1, min(last_idx+1, farthest+1)):
                if i + nums[i] >= farthest:
                    farthest = i + nums[i]
                    cur = i
                if farthest >= last_idx:
                    break
            steps += 1    
        return steps