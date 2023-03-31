class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = False
        indx = 1
        if n & 1 == 0:
            flag = True
        while n > 0:    
            if flag:
                if n & 1 == 1:
                    print(bin(n))
                    return False
                flag = False
            else:
                if n & 1 == 0:
                    return False
                flag = True
            n >>= 1

        return True
