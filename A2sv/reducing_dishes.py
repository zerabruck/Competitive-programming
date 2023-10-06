class Solution:
    def combination (self, index, time):
        if index >= len(self.sat):
            return 0

        if (index, time) not in self.dp:
            choose = (self.sat[index] * time ) + self.combination(index + 1, time + 1)
            not_choose = self.combination(index + 1, time)
            self.dp[(index, time)] = max(choose, not_choose)

        return self.dp[(index, time)]
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        self.sat = satisfaction
        self.dp = {}
        val = self.combination(0, 1)
        return val       
