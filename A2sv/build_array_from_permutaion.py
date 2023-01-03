class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        [ result.append(nums[i]) for i in nums ]
        return result