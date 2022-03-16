from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # key: number in nums2, value: next greater number of key in nums2
        next_greater = defaultdict(lambda:-1) 
    
        monotonic_stack = []
        for idx, num2 in enumerate(nums2):
            while monotonic_stack and num2 > monotonic_stack[-1]:
                next_greater[monotonic_stack.pop()] = num2
            monotonic_stack.append(num2)
            
        ans = []
        for num1 in nums1:
            ans.append(next_greater[num1])
        return ans
