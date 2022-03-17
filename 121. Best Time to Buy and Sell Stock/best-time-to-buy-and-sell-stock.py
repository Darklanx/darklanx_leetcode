'''
We can choose one of the n days to purchase
and sell in some future day
'''
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = -math.inf
        max_after = -math.inf
        for price in reversed(prices):
            max_profit = max(max_profit, max_after - price)
            max_after = max(price, max_after)
            
            
        return max(max_profit, 0)
            