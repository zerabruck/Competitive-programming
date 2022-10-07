class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if(k==0):
            nums.append(0)
        
        
        max_len=0
        zero_index_array=[]
        nums_zero=0
        beg=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums_zero+=1
                zero_index_array.append(i)



            if nums_zero>k:  

                arr=nums[beg:i]   

                max_len=max(max_len,len(arr))
                beg=zero_index_array.pop(0)+1
                nums_zero-=1
                
            if(i==len(nums)-1 and nums_zero==k):

                arr=nums[beg:i+1]  

                max_len=max(max_len,len(arr))

        if(beg==0):
            max_len=len(nums)
        return max_len