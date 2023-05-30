class Solution:
    def target_sum(self, index, target):
        if index >= len(self.nums):
            if target == 0:
                return 1
            else:
                return 0

        if (index, target) not in self.dicto:
            sub = self.target_sum(index + 1, target - self.nums[index])
            add = self.target_sum(index + 1, target + self.nums[index])
            self.dicto[(index, target)] = sub + add 
        return self.dicto[(index, target)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dicto = {}
        self.nums = nums
        return self.target_sum(0, target)
