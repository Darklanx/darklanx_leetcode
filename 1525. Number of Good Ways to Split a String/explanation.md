[1525. Number of Good Ways to Split a String](https://leetcode.com/problems/number-of-good-ways-to-split-a-string)
===
$O(n)$
We store unique characters starting of left substrings to an array,
e.g.
```
abcab
12333
```
and then we do so for the right sub string as well
e.g.
```
abcab
22321
```
then if
l_count[i] = r_count[i+1] (careful for i+1 out of bound)
it's a valid split.