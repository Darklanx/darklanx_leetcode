'''
Time: O(len(coins) * amount)
space:  O(amount)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount+1)]
        dp[0] = 0
        for remaining_amount in range(amount + 1):
            _min = math.inf
            for coin in coins:
                if remaining_amount - coin >= 0:
                    dp[remaining_amount] = min(dp[remaining_amount - coin] + 1, dp[remaining_amount])

        return int(dp[-1]) if dp[-1] != math.inf else -1

