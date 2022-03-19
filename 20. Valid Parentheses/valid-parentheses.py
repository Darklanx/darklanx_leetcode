from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in mapping:
                top = stack.pop() if stack else '#'
                if top != mapping[ch]:
                    return False
            else:
                stack.append(ch)
            
        return len(stack) == 0
        