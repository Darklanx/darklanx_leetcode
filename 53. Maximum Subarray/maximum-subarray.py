class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        max_before = 0
        for num in nums:
            max_before = max(num, max_before + num)
            if max_before > _max:
                _max = max_before
        return _max