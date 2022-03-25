[1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain)
===
### Time complexity: $O(n * l^2)$
1. We know that words with length `l` will have predecessors of length `l-1`.
2. We store the longest_chain length starting with `word` in `len_chain[word]`.
3. Starting from the words with longest length, we iteratively update `len_chain[predecessor]` by `len_chain[predecessor] = len_chain[current_word] + 1`

Why do it from the longest words?
Because it is easier to find predecessors of word `w` than to find suceccessors of a word.
Ex:
word = 'abc'
predecessors = ['ac', 'bc' , 'ac']
```
for i in range(len(word)):
    preds.append(word[0:i] + word[i+1:])
```
Which takes $O(l)$

However if we want to find all successors of a word,
let word = 'ab'
It will be the form of '\$ab', 'a\$b', 'ab\$'.
which takes $O(l* 26)$.
