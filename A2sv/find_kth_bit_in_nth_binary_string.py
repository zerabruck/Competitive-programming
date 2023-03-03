class Solution:
    def bit_finder(self , n): 
        if n == 1 :
            return "0"

        elif n == 2 :
            return "011"

        prev = self.bit_finder( n - 1)
        inverted = prev[:len(prev) // 2] + '0' + prev[(len(prev) // 2) + 1 : ]
        return prev + '1' + inverted
    def findKthBit(self, n: int, k: int) -> str:
        return self.bit_finder(n )[k - 1]     
