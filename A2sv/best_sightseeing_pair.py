class Solution:
    def spots(self, i, j):
        return self.values[i] + self.values[j] + i - j

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        self.values = values
        dp = [0]
        max_val = 0
        for value in range(1, len(values)):
            val_index = 0
            if self.spots(dp[-1], value) > self.spots(value - 1, value):
                val_index = dp[-1]
            else:
                val_index = value - 1
            max_val = max(max_val,  self.spots(dp[-1], value), self.spots(value - 1, value))
            dp.append(val_index)
        return max_val
