class Solution:
    def subseq(self, index, prev, diff):
        if index >= len(self.nums):
            return 0

        if (index, prev, diff) not in self.dp:
            not_choose = self.subseq(index + 1, prev, diff)
            choose = 0
            if prev == -1:
                choose = 1 + self.subseq(index + 1, index, diff)
            elif diff == 501:
                choose = 1 + self.subseq(index + 1, index, self.nums[prev] - self.nums[index])
            elif diff == (self.nums[prev] - self.nums[index]):
                choose = 1 + self.subseq(index + 1, index, diff)
            self.dp[(index,prev,diff)] = max(choose, not_choose)
        return self.dp[(index, prev, diff)]


    def longestArithSeqLength(self, nums: List[int]) -> int:
        self.dp = {}
        self.nums = nums
        return self.subseq(0, -1, 501)
