class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        max_len=0
        count=0
        index=0
        beg=0

        for i in range(len(nums)+1):
            if(i==len(nums)):
                length=i-beg-1
                max_len=max(max_len,length)
                beg=index+1
                index=i
                break
            elif(nums[i]==0 and count==0):
                count+=1
                index=i

            elif(nums[i]==0 and count==1 ):
                length=i-beg-1
                max_len=max(max_len,length)
                beg=index+1
                index=i

        if(count==0):
            max_len=len(nums)-1
            
        return max_len
