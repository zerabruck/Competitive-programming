class Solution:
    def powerr(self,x,n,dicto):

        if n not in dicto:
            if n == 1:
                
                dicto[n] = x
                return x

            val = n//2
            returned = self.powerr(x , val,dicto) * self.powerr(x , n - val,dicto)
            dicto[n] = returned

            return returned

        else:
            return dicto[n]

    def myPow(self, x: float, n: int) -> float:
        
        dicto = {}
        if n < 0:
            return self.powerr(1/x , (-1 * n) , dicto)
        elif n == 0:
            return 1
        else:     
            return self.powerr(x,n,dicto)       
