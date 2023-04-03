class Solution:
    def bitwise_or(self , nums) -> int:
        val = 0
        for num in nums:
            val |= num
        return val
    def combinations(self, nums , traveld , idx):
        if idx >= len(nums):
            val = self.bitwise_or(traveld)
            if val > self.max_val:
                self.count_val = 1
                self.max_val = val
            elif val == self.max_val:
                self.count_val += 1
            return

        traveld.append(nums[idx])
        self.combinations(nums , traveld , idx + 1)
        traveld.pop()
        self.combinations(nums , traveld , idx + 1)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.count_val = 0
        self.max_val = 0
        self.combinations(nums , [] , 0)
        return self.count_val
