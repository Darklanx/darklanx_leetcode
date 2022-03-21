from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        keys = set(c1.keys()) | set(c2.keys())
        for key in keys:
            if c1[key] != c2[key]:
                return False
        return True