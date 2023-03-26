class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first = 0
        while first < len(nums):
            indx = nums[first] - 1
            if first == nums[first] - 1:
                first += 1
            elif nums[first] == nums[indx]:
                return nums[first]
            else:
                nums[first] , nums[indx] = nums[indx] , nums[first]
