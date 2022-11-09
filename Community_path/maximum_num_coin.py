class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
          
        piles.sort()
        result=0
        
        while(len(piles)!=0):
            piles.pop()
            second=piles.pop()
            result+=second
            piles.pop(0)
        
            
            
        return result
