class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        tuple_freq=[]
        count=1
        if(len(nums)==1):
            return nums
        for i in range(1,len(nums)):
            
            if(nums[i]==nums[i-1]):
                count+=1
                if(i==len(nums)-1):
                    tuple_freq.append((nums[i],count))
                    
            else:
                tuple_freq.append((nums[i-1],count))
                if(i==len(nums)-1):
                    tuple_freq.append((nums[i],count))
                count=1
            
            
        tuple_freq.sort(reverse=True,key= lambda x:x[1])
        result=[]
        print(tuple_freq)
        for i in range(k):
            result.append(tuple_freq[i][0])
            
        return result
