from collections import namedtuple

IndexNum = namedtuple('index_num', ['index', 'num'])
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        _max = max(nums)
        ori_n = len(nums)
        id_nums = [IndexNum(idx, num) for idx, num in enumerate(nums)] * 2
        mono_stack = []
        
        ans = [-1 for i in range(ori_n)]
        for i, (num_idx, num) in enumerate(id_nums):

            while mono_stack and num > mono_stack[-1].num:
                ans[mono_stack.pop().index] = num
                
        
            if i < ori_n and num < _max:
                mono_stack.append(IndexNum(num_idx, num))
            elif num == _max:
                ans[num_idx] = -1
        
        return ans
            