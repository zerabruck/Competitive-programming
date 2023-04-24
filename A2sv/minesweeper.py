class Solution:
    def in_bound(self, row , col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def dfs(self, row , col):
        if self.board[row][col] == 'M':
            self.board[row][col] = 'X'
            return

        count = 0
        self.visited.add((row , col))
        for row_val , col_val in self.directions:
            row_d = row_val + row
            col_d = col_val + col
            if self.in_bound(row_d , col_d) and self.board[row_d][col_d] == 'M':
                count += 1
        if count != 0:
            self.board[row][col] = str(count)
        else:
            self.board[row][col] = "B"
            for row_val , col_val in self.directions:
                row_d = row_val + row
                col_d = col_val + col
                if self.in_bound(row_d , col_d) and (row_d , col_d) not in self.visited:
                    self.dfs(row_d , col_d)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board = board
        self.directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]
        self.visited = set()
        self.dfs(click[0], click[1])
        return self.board
