#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
## abcde
## axxce
# @lc code=start
from os import stat


class Solution:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        mem = [[-1 for _ in range(m)] for _ in range(n)]
        def recursion(i1: int, i2: int) -> int:
            if i1 >= n or i2 >= m:
                return 0
            if mem[i1][i2] != -1:
                return mem[i1][i2]
            case1 = case2 = case3 = 0

            if text1[i1] == text2[i2]:
                case1 = recursion(i1+1, i2+1) + 1
            else:
                case2 = recursion(i1, i2+1)
                case3 = recursion(i1+1, i2)
            mem[i1][i2] = max(case1 , case2, case3)
            return mem[i1][i2]
            
        return recursion(0, 0)
        
# @lc code=end
l1 = "ylqpejqbalahwr"
l2 = "yrkzavgdmdgtqpg"
print(Solution.longestCommonSubsequence(l1, l2))