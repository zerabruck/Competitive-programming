class Solution:
    def falling_path(self, row, col):
        if row >= len(self.matrix):
            return 0
        if col < 0 or col >= len(self.matrix):
            return inf
        if (row, col) not in self.dp:
            down_left = self.falling_path(row + 1, col - 1)
            down = self.falling_path(row + 1, col )
            down_right = self.falling_path(row + 1, col + 1)
            self.dp[(row, col)] = self.matrix[row][col] + min(down_left, down, down_right)
        return self.dp[(row, col)]
            

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.dp = {}
        self.matrix = matrix
        path = inf
        for col in range(0, len(matrix)):
            path = min(path, self.falling_path(0, col))
        return path 
