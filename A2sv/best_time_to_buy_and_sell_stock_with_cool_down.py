class Solution:
    def stock_exchange(self, index, status):
        if index >= len(self.prices):
            return 0
        if (index, status) not in self.dp:
            not_choose = self.stock_exchange(index + 1, status)
            choose = 0
            if status == 0:
                choose = - self.prices[index] + self.stock_exchange(index + 1, 1)
            else:
                choose = self.prices[index] + self.stock_exchange(index + 2, 0)
            self.dp[(index, status)] = max(not_choose, choose)
        return self.dp[(index, status)]

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.dp = {}
        return self.stock_exchange(0, 0)    
