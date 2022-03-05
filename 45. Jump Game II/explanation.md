[45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
===
#### Time complexity: $O(n)$ 
Jumping from left, for each step, we can jump at most `nums[i]` distance.
The question is, where should we jump to.
Taking the greedy approach, we can always jump to the target, that have the farthest reach.
For example: `[2, 3, 1, 0]`
When in location `0`, we can reach location `1` & `2`:
1. Location `1` can reach `1 + 3 = 4`
2. Location `2` can reach `2 + 1 = 3` 

So we should jump to location `1`, repeat this pattern then we can reach the goal in least jumps.



P.S. There's a $O(n^2)$ solution that AC.
