class Solution:
    def steps(self, index, paste_val):
        if index > self.n:
            return inf
        if index == self.n:
            return 0

        if (index, paste_val) not in self.dp:
            copy_and_paste = 2 + self.steps(index + index, index)
            paste = inf
            if paste_val != -1:
                paste = 1 + self.steps(index + paste_val, paste_val)
            self.dp[(index, paste_val)] = min(copy_and_paste, paste)
        return self.dp[(index, paste_val)]
    def minSteps(self, n: int) -> int:
        self.dp = {}
        self.n = n
        if n == 1:
            return 0
        return self.steps(1, -1)  
