class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[0]]]
        for index in range(1, len(nums)):
            max_len = []
            for prev in range(index - 1, -1, -1):
                if nums[index] % dp[prev][-1] == 0 and len(dp[prev]) > len(max_len):
                    max_len = dp[prev]
            copied = max_len.copy()
            copied.append(nums[index])
            dp.append(copied)
        largest = []
        for ele in dp:
            if len(ele) > len(largest):
                largest = ele
        return largest
