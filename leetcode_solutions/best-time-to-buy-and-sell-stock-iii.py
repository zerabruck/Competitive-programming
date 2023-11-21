class Solution:
    def stocks(self, index, status):
        if status >= 5:
            return 0
        if index >= len(self.prices):
            return 0

        if (index, status) not in self.dp:
            not_choose = self.stocks(index + 1, status)
            choose = 0
            if status % 2 == 0:
                choose = self.prices[index] + self.stocks(index + 1, status + 1)
            else:
                choose = -self.prices[index] + self.stocks(index + 1, status + 1)
            self.dp[(index, status)] = max(not_choose, choose)
        return self.dp[(index, status)]


    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}
        self.prices = prices
        res = self.stocks(0, 1)
        return res     