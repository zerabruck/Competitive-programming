class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        first_pre_fix=[1]
        second_pre_fix=[1]
        newArray=[]


        for i in range(len(nums)):
            first_pre_fix.append(first_pre_fix[i]*nums[i])
            second_pre_fix.append(second_pre_fix[i]*nums[len(nums)-1-i])




        for i in range(1,len(first_pre_fix)):
            newArray.append(first_pre_fix[i-1]*second_pre_fix[len(first_pre_fix)-i-1])
            
        return newArray

