class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ele_dict = {}
        dp = [0] * len(nums)
        dp[0] = 1
        ele_dict[0] = 1
        for index in range(1, len(nums)):
            max_val = 0
            max_ele = 0
            for prev in range(index - 1, -1, -1):
                if nums[index] > nums[prev] and dp[prev] == max_val:
                    max_ele += ele_dict[prev]
                elif nums[index] > nums[prev] and dp[prev] > max_val:
                    max_val = dp[prev]
                    max_ele = ele_dict[prev]
            if max_ele == 0:
                ele_dict[index] = 1
            else:
                ele_dict[index] = max_ele
            dp[index] = max_val + 1
      
        max_val = max(dp)
        largest_count = 0
        for index in range(len(nums)):
            if dp[index] == max_val:
                largest_count += ele_dict[index]
        return largest_count      
