class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        result=[]
        
        for i in range(len(l)):
            value=list(nums[l[i]:r[i]+1])
            value.sort()
            first=value[1] -value[0]
            for i in range(len(value)-1):
                if(value[i+1]-value[i]!=first):
                    result.append(False)
                    value.clear()
                    break
                    
                elif(i==len(value)-2):
                    result.append(True)
                    value.clear()
                    
            
        return result
                    
                
        