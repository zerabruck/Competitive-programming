class Solution:
    def trib(self, n):
        if n == 0:
            return n
        if n == 1:
            return n
        if n == 2:
            return 1
        if n not in self.dicto:
            self.dicto[n] = self.trib( n - 1 ) + self.trib(n - 2) + self.trib(n - 3)
        return self.dicto[n]
            
    def tribonacci(self, n: int) -> int:
        self.dicto = {}
        return self.trib(n) 
