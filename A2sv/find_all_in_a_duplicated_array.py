class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        first = 0
        while first < len(nums):
            if nums[first] == 0 or nums[first] - 1 == first :
                first += 1
            elif nums[nums[first] - 1 ] == nums[first] :
                res.append(nums[first])
                nums[first] = 0
                first += 1
            else:
                val = nums[first] - 1
                nums[first] , nums[val] = nums[val] , nums[first]
        return res
