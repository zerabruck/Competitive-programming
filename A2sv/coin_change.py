class Solution:
    def simulation(self,amount):
        if amount < 0:
            return 10**5
        if amount == 0:
            return 0
        
        if amount not in self.dicto:
            min_coin = inf
            for coin in self.coins:
                res = self.simulation(amount - coin)
                min_coin = min(min_coin, res)
            self.dicto[amount] = min_coin + 1
        return self.dicto[amount]  
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.dicto = {}
        num_coin = self.simulation(amount)
        if num_coin >= 10**5:
            return -1
        return num_coin
