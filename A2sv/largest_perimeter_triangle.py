class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        for index,value in enumerate(nums):
            if(index+2<=len(nums)-1):
                summ=nums[index+1] + nums[index+2]
                if(value<summ):
                    return value+ summ

            else:
                return 0