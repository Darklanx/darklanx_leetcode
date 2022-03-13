[91. Decode Ways](https://leetcode.com/problems/decode-ways)
===
Observations:
    1. We can group 2 digits, but never 3.
    2. If there's a 0 in s at s[i], it must be grouped with s[i-1]. (unless it's invalid, e.g. `s[i-1] == 0` or `s[i-1] >= 3`)
    3. Because of (2), we can actually remove s[i-1] and s[i] since it does not affect the solution.
    4. Because of (1), "1234" can be found by all combination of "123" + single "4" 
        and all combination of "12" + "34" (if "34" is valid, which is not in this case)

so if we let `n_decode[i] = numbers of way to decode s[0:i]`
then `n_decode[i] = n_decode[i-1] + is_valid(s[i-1] + s[i]) * n_decode[i-2]`