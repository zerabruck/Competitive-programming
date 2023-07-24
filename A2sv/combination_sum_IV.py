class Solution:
    def combination(self, target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target not in self.dp:
            value = 0
            for num in self.nums:
                value += self.combination(target - num)
            self.dp[target] = value
        return self.dp[target]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = {}
        self.nums = nums
        return self.combination(target)
