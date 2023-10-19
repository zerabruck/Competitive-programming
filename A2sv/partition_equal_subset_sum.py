class Solution:
    def subset(self, index, target):
        if target == 0:
            return True
        if index >= len(self.nums):
            return False
        if (index, target) not in self.dp:
            choose = self.subset(index + 1, target - self.nums[index])
            not_choose = self.subset(index + 1, target)
            self.dp[(index, target)] = choose or not_choose
        return self.dp[(index,target)]
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.dp = {}
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        return self.subset(0, sums // 2)   
