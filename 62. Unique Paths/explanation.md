[62. Unique Paths](https://leetcode.com/problems/unique-paths)
===
Solution is compressed with 2 row dp.
At every position `[i][j]`, number of possible paths 
= sum of number of possible paths for `[i+1][j]` (down) & `[i][j+1]` (right).