class Solution:
    def wiggle(self, index, prev, sign):
        if index >= len(self.nums):
            return 0

        if (index, prev, sign) not in self.dp:
            not_choose = self.wiggle(index + 1, prev, sign)
            choose = 0
            if prev == -1:
                choose = 1 + self.wiggle(index + 1, index, -1)
            elif sign == -1 and self.nums[prev] != self.nums[index]:
                val_sign = 0
                if self.nums[prev] - self.nums[index] > 0:
                    val_sign = 1
                choose = 1 + self.wiggle(index + 1, index, val_sign )

            elif sign == 0 and self.nums[prev] > self.nums[index]:
                choose = 1 + self.wiggle(index + 1, index , 1)
            elif sign == 1 and self.nums[prev] < self.nums[index]:
                choose = 1 + self.wiggle(index + 1, index, 0)

            self.dp[(index, prev, sign)] = max(choose, not_choose)
        return self.dp[(index, prev, sign)]
    def wiggleMaxLength(self, nums: List[int]) -> int:
        self.dp = {}
        self.nums = nums
        val = self.wiggle(0, -1, -1)
        return val   
