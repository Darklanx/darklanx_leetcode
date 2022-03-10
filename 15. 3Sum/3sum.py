class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums, target_sum):
            l = 0
            r = len(nums)-1
            l_set, r_set = set(), set()
            two_sum_list = []
            while l < r:
                if nums[l] in l_set:
                    l += 1
                    continue
                if nums[r] in r_set:
                    r -= 1
                    continue
                
                two_sum = nums[l] + nums[r]
                if two_sum == target_sum:
                    two_sum_list.append([nums[l], nums[r]])
                    l_set.add(nums[l])
                    r_set.add(nums[r])
                elif two_sum < target_sum:
                    l_set.add(nums[l])
                    l += 1   
                elif two_sum > target_sum:
                    r_set.add(nums[r])
                    r -= 1
                    
            return two_sum_list
                
        nums.sort()
        num_set = set()
        idx = 0
        tri_list = []
        while idx < len(nums):
            num = nums[idx]
            if num in num_set:
                idx += 1
                continue
            
            num_set.add(num)
            target_sum = 0 - num

            two_sum_list = two_sum(nums[idx+1:], target_sum)
            for two in two_sum_list:
                tri_list.append(two + [num])
            idx += 1
        
        return tri_list
                
            
            
        
        