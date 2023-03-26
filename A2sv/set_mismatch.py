class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        first = 0
        dup = None
        while first < len(nums):
            val = nums[first] - 1
            if nums[first] < 0:
                first += 1
            elif val == first:
                first += 1
            elif nums[first] == nums[val] :   
                nums[first] *= -1
                dup = nums[first] 
                first += 1
            else:
                nums[first] , nums[val] = nums[val] , nums[first]
        for indx , val in enumerate(nums):
            if val == dup:
                return [dup * -1 , indx + 1]          
