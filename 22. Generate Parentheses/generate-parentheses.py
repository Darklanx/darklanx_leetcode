class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen(cur_l, left, right):
            nonlocal n, ans
            if left == n and right == n:
                ans.append(''.join(cur_l))
                return
            if left < n:
                cur_l.append('(')
                gen(cur_l, left+1, right)
                cur_l.pop()
            
            if left > right:
                cur_l.append(')')
                gen(cur_l, left, right+1)
                cur_l.pop()
            
        
        ans = []
        gen([], 0, 0)
        
        return ans
        