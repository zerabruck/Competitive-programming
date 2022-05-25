class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        counter=0
        result=0
        while(counter!=len(nums)-1):
            position=counter+1
            if(nums[counter]>=nums[position]):
                values=nums[counter] - nums[position]
                result+=values+1
                nums[position]+=values+1
            else:
                counter+=1
        return result
