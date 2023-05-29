class Solution:
    def gen(self, n):
        if n < 2:
            return n
        if n not in self.dicto:
            if n % 2 == 0:
                self.dicto[n] = self.gen(n // 2)
            else:
                self.dicto[n] = self.gen(n // 2) + self.gen((n // 2) + 1)
        return self.dicto[n]
        
    def getMaximumGenerated(self, n: int) -> int:
        self.dicto = {}
        res = []
        for i in range(n , -1, -1):
            if i not in self.dicto:
                res.append(self.gen(i))
        return max(res)
