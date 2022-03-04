[55. Jump Game](https://leetcode.com/problems/jump-game/)
===
The most intuitive method is to loop from the last position, and store the farthest position that `pos(i)` can arrive.
For position $i$, we store the farthest position it can reach within the coverage `i to i+num[i]` *with a for loop*.
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        l = len(nums)
        nums[-1] = l-1 # last index
        for i in reversed(range(l)): 
            step = nums[i]  # max look forward, l-i to avoid invalid index)
            nums[i] = i
            for j in range(1, min(step + 1, l-i)):
                nums[i] = max(nums[i], nums[i + j])
                if nums[i] >= l-1:
                    break
        return nums[0] >= l-1
```

However there's a better solution that can avoid such for loop.
We loop from the last position like before, however we keep track of the minimum index `min_index` that can reach to the goal.
Initially `min_index=len(nums)-1` since the last positive can definitely reach to itself.
Then for every `i`, we check if `i + nums[i] >= min_index`, if true, then position `i` can also reach the goal, so we update `min_index = i`.
In the end, if `min_index == 0` then we can reach the goal starting from the first position.