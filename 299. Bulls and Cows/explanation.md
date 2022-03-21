[299. Bulls and Cows](https://leetcode.com/problems/bulls-and-cows)
===
Iterate over the strings: s is the current character in the string secret and g - the current character in the string guess.

`If s == g`, update bulls counter: `bulls += 1.`

Otherwise, `if s != g:`

Update cows by adding 1 if so far guess contains more s characters than secret: `counter[s] < 0`.

Update cows by adding 1 if so far secret contains more g characters than guess: `counter[g] > 0`.

Update the hashmap by marking the presence of s character in the string secret: `counter[s] += 1`.

Update the hashmap by marking the presence of g character in the string guess: `counter[g] -= 1`.

- Note that when `counter[ch] < 0`, then `guess` has seen more `ch` than `secret`.