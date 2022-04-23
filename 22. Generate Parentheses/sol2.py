class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            return ['']
        
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-i-1):
                    ans.append(f"({left}){right}")
        
        return ans