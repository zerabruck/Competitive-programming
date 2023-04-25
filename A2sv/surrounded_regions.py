class Solution:
    def in_bound(self , row , col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])
    def dfs(self , row , col):
        if (row,col) in self.visited:
            return
        self.visited.add((row,col))
        self.board[row][col] = "F"
        for row_val , col_val in self.directions:
            row_d = row_val + row
            col_d = col_val + col
            if self.in_bound(row_d , col_d) and self.board[row_d][col_d] == "O":
                self.dfs(row_d , col_d)

    def solve(self, board: List[List[str]]) -> None:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.board = board
        self.visited = set()
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == "O":
                    if 0 == row or row == len(self.board) - 1 or 0 == col or col == len(self.board[0]) - 1:
                        self.dfs(row , col)
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == "F":
                    self.board[row][col] = "O"
                else:
                    self.board[row][col] = "X"
        """
        Do not return anything, modify board in-place instead.
        """
