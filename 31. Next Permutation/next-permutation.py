# [1 4 2 1] => [1 1 2 1]
# [1 2 4 3 1] => [1 3 1 2 4]
# 1. Loop from behind, find the first number is break the monotonic sequence
# ex. [1 2 4 3 1], 2 breaks the monotonic sequence of [1 3 4]
# swap it with the first larger num, and sort the remaining sequence
# ex: 4 > 3 > 2 => swap with swap 2 with 3 and sort [1 2 4]
# => [1 3 1 2 4]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def upper_bound(nums, l, r, base):
            '''
            assume nums[l:r] is in decreasing order
            '''
            while l < r:
                mid = (l + r) // 2
                
                if nums[mid] > base:
                    l = mid + 1
                    if l >= len(nums) or nums[l] <= base:
                        return l-1
                else:
                    r = mid -1 
            return l
            
        
        n_nums = len(nums)
        if n_nums <= 1:
            return nums
        
        _max = nums[-1]
        found = False
        for idx in reversed(range(n_nums)):
            if nums[idx] < _max:
                # swap nums[idx] with the number just larger in nums[idx+1:]
                swap_idx = upper_bound(nums, idx+1, n_nums, nums[idx])
                tmp = nums[idx]
                nums[idx] = nums[swap_idx]
                nums[swap_idx] = tmp
                nums[idx+1:] = sorted(nums[idx+1:])
                found = True
                break
            else:
                _max = max(_max, nums[idx])
                
        if not found:
            nums.sort()
            
        return nums
            