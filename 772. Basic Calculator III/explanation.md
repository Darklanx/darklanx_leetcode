[772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii)
===
1. We always perform `* and /` whenever we can.
2. Whenever we insert a number, if the next character is not `* or /`, then we can perform all operator currently in the stack. 
If the next character is `* or /`, we perform operation only if the previous operator  is `* or /`
3. If ')' is encountered, we handle every thing between the parentheses, after the parentheses is evaluated, insert the number as in (2).
In the end, the stack will consists of only `+ and -`, because all parentheses and `*/` were handled.