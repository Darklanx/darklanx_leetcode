# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
## [iterate.py](https://github.com/Darklanx/darklanx_leetcode/blob/main/22.generate-parentheses/iterate.py)
We insert '(' or ')' iteratively, while keeping track the number already inserted.

## [set.py](https://github.com/Darklanx/darklanx_leetcode/blob/main/22.generate-parentheses/set.py)
When generating n parentheses, we consider cases
() n-1, (1) n-2, (2) n-3...
we use set to avoid duplicates
 
