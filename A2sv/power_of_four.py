elements = set()
for i in range(17):
    elements.add(4**i)
class Solution:
    # def power(self , pow , n):
    #     over = 4 ** pow
    #     if over > n :
    #         return False
    #     elif over == n:
    #         return True
    #     return self.power( pow + 1,n)

    def isPowerOfFour(self, n: int) -> bool:
        # if n < 1 :
        #     return False
        # elif n == 1:
        #     return True    
        return n in elements
