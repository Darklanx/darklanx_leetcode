class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n_comb_for_amnt = [0 for i in range(amount+1)]
        n_comb_for_amnt[0] = 1
        for coin in coins:
            for i in range(coin, len(n_comb_for_amnt)):
                n_comb_for_amnt[i] += n_comb_for_amnt[i - coin]
        return n_comb_for_amnt[amount]
        
