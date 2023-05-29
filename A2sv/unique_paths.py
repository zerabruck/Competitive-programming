class Solution:
    def in_bound(self, row, col):
        return 0 <= row < self.m and 0 <= col < self.n

    def backtrack(self, row, col):
        if not self.in_bound(row, col):
            return 0
        if row == self.m - 1 and col == self.n - 1:
            return 1
        if (row, col) not in self.dicto:
            self.dicto[(row,col)] = self.backtrack(row + 1, col) + self.backtrack(row, col + 1)
        return self.dicto[(row,col)]       

    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.dicto = {}
        return self.backtrack(0, 0)
