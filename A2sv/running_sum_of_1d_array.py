class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for num in range(1,len(nums)):
            nums[num] += nums[num - 1]

        return nums
