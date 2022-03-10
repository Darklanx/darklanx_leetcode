class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not hasattr(self, 'table'):
            self.table = {}
        key = str(amount) + "," + str(len(coins))
        if key in self.table:
            return self.table[key]
        
        coin = coins[-1]
        # we know amount >= 0,
        if amount == 0:
            return 1
        # avoid sending len(coins) == 0 to next level
        if len(coins) == 1:
            if amount % coin == 0:
                return 1
            else:
                return 0
             
        n_ways = 0
        n_coin = 0
        while True:
            if amount - n_coin*coin < 0:
                break
            n_ways += self.change(amount - n_coin*coin, coins[0:-1])
            n_coin += 1
        self.table[key] = n_ways
        return n_ways