from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(l: list, s: str, left: int, right: int):
            if  left > right:
                return
            if left == 0 and right == 0:
                l.append(s)
            else:
                if left > 0:
                    generate(l, s + "(", left-1, right)
                if right > 0: 
                    generate(l, s + ")", left, right-1)
        l = []
        s = ""
        generate(l, s, n, n)
        
        return l
            