[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)
===
1. Find the smallest `r` such that `s[0:r+1]` is valid.
2. Find the largest `l` such that `s[l:r+1]` is valid, note that at this point, `s[l:r+1]` is the shortest substring of `s[0:r+1]` satisfying condition.
3. With (2), we know `s[l+1:r+1]` is invalid, but we can search for a new `r'` such that `s[l+1:r'+1]` is valid.
4. Repeat (2) - (3)


### Time complexity: $O(|S| + |T|)$)
1. Finding the minimal valid set => $O(|S|)$
2. Second while loop is a two pointer, which is $O(|S|)$

However we have looped through both `s` and `t` with $O(|S|)$ and $O(|T|)$.

### Space complexity: $O(|S| + |T|)$):
`Counter(S) and Counter(T)`

