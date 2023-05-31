class Solution:
    def houses(self, index):
        if index == 0:
            return self.nums[index]
        if index == 1:
            return  max(self.nums[0], self.nums[1])

        if index not in self.dicto:
            op1 = self.houses(index - 1)
            op2 = self.houses(index - 2) + self.nums[index]
            self.dicto[index] = max(op1, op2)
        return self.dicto[index]
    def rob(self, nums: List[int]) -> int:
        self.dicto = {}
        self.nums = nums
        self.flag = 1
        if len(nums) < 4:
            return max(nums)
        first = self.houses(len(nums) - 2)
        self.nums.pop(0)
        self.dicto = {}
        second = self.houses(len(nums) - 1)
        return max(first, second)
