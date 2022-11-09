class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        beg=0
        end=len(nums)-1
        maximo=0
        while(beg<end):
            value=nums[beg]+nums[end]
            maximo=max(maximo,value)
            beg+=1
            end-=1
            
        return maximo
            
        