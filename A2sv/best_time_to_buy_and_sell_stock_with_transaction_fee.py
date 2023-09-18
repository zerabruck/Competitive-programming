class Solution:
    def subseq(self,index, flag):
        if index >= len(self.prices):
            return 0
        if (index, flag) not in self.dp:
            not_choose = self.subseq(index + 1, flag)
            choose = 0
            if flag == 0:
                choose = -self.prices[index] + self.subseq(index + 1, 1)
            if flag == 1:
                choose = self.prices[index] - self.fee + self.subseq(index + 1, 0)
            self.dp[(index, flag)] = max(not_choose, choose)
        return self.dp[(index, flag)]
    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.prices = prices
        self.fee = fee
        self.dp = {}
        return self.subseq(0, 0)
