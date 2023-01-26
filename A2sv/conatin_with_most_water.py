class Solution:
    def maxArea(self, height: List[int]) -> int:

        beg=0
        end=len(height)-1
        result=0
        
        while(beg<end):
            
            area=(end-beg)*min(height[beg],height[end]) 
            result=max(result,area)
            
            if(height[beg]>height[end]):
                end-=1
            else:
                beg+=1
                
                
        return result
            
            
