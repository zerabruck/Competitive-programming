class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count=0
        firstsum=sum(arr[:k])
        if(firstsum/k>=threshold):
            count+=1

        for i in range(k,len(arr)):
            sub_arr=firstsum-arr[i-k]
            add_arr=sub_arr+arr[i]

            firstsum=add_arr
            if(firstsum/k>=threshold):
                count+=1
                
        return count


