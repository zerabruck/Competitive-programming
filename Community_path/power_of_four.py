class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(value):
            if(value==1):
                return True
            elif(value%4!=0):
                return False
            elif(value<4):
                return False
            return power(value//4)
        return power(n)