class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def power(value):
            if(value==1):
                return True
            elif(value%3!=0):
                return False
            elif(value<3):
                return False
            return power(value//3)
        
        return power(n)
        
        
        
            
            

        