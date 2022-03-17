[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)
===
This question make use of a similar idea as [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray).

Consider two array, `max_nums` and `min_nums`
`max_nums[i]` stores the maximum product we can find by only considering `nums[0:i+1] (num0 ~ numi)`, while including `nums[i]`.
Once we have `max_nums[i] & min_nums[i]`, we can calculate `max_nums[i+1] & min_nums[i+1]`.
We know that `max_nums[i+1]` either is `nums[i+1]`, or it is some number by multiplying `nums[i+1]` with `nums[i] or nums[i]*nums[i-1] or nums[i]*nums[i-1]*nums[i-2] ... etc`.

However, since we know that `nums[i+1]` is either positive or negative.
1. If it is positive, then `max_nums[i+1]` will be `max(nums[i+1], max_nums[i] * nums[i+1])`, `min_nums[i+1] = min(nums[i+1], min_nums[i] * nums[i+1])`.
2. If it is negative, then `max_nums[i+1]` will be `max(nums[i+1], min_nums[i] * nums[i+1])`, `min_nums[i+1] = min(nums[i+1], max_nums[i] * nums[i+1])`.

Thus, by recording the max number that we observe during the process, we have the solution.