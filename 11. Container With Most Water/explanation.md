[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water)
===
Time: $O(n)$
Two pointers:
We start with `l = 0, r = n-1`, and we can obtain the first area.
Note that if `height[l] < height[r]`, moving `r` will never obtain a larger area, since the width `r-l` becomes smaller, while `min(height[l], height[r]) <= height[l]`.
Thus it is only possible to find a better solution by moving `l`.
Following this logic and move the point that have smaller height and store the largest area than the problem is solved.

(What if `height[l] == height[r]`? It can be shown that moving either is fine!)

