class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        beg=0
        end=len(nums)-1
        result=0
        
        while(True):
            if(beg>end or beg==end):
                break
                
            value=nums[beg]+nums[end]
            
            
            if(value==k):
                result+=1
                beg+=1
                end-=1
                
            elif(value>k):
                end-=1
                
            elif(value<k):
                beg+=1
                
                
        return result
                
            
                
            
        