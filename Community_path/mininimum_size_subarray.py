class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        pref_sum=[0,nums[0]]
        
        for i in range(1,len(nums)):
            pref_sum.append(nums[i]+pref_sum[i])
            
        minn=-1
        pointer=0
            
        
        for i in range(len(pref_sum)):
            if(pref_sum[i]>=target):   
                for j in range(pointer,i+1):
                    pointer=j
                   
                            
                    if(pref_sum[i]-pref_sum[j]>=target):
                        if(minn<0):
                            
                            
                            minn=i-j
                            continue
                            
                        old_min=minn
                        
                      
                        minn=min(minn,i-j)
                        new_min=minn
                        
                        
                        
                        
                    if(pref_sum[i]-pref_sum[j]<target):
                        break
                        
                        
        if(minn<0):
            return 0
                        
        return minn
            
        