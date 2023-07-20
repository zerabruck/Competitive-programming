class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        min_price = prices[0]
        profit = 0

        for index in range(1, len(prices)):
            if prices[index] < min_price:
                min_price = prices[index]

            elif prices[index] - min_price > profit:
                profit = prices[index] - min_price

        return profit
