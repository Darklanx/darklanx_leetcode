from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        counter = Counter()
        for idx, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                bulls += 1
            else:
                cows += int(counter[s] < 0) + int(counter[g] > 0)
                counter[s] += 1
                counter[g] -= 1

                
        return f"{bulls}A{cows}B"
                