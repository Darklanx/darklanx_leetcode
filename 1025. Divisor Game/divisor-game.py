# n = 1 : False
# n = 2 : True
# n = 3 : False
# n = 4 : 4->2 or 4->3 : True
from functools import cache
class Solution:

    @staticmethod
    @cache
    def divisorGame(n: int) -> bool:
        if n == 1:
            return False

        winnable = False
        for i in range(1, n):
            if n % i == 0:
                winnable = winnable or not Solution.divisorGame(n - i)
        return winnable
                
            
        