class Solution:
    def is_bound(self , row , col):
        return 0 <= row < len(self.grid2) and 0 <= col < len(self.grid2[0])

    def dfs(self, row , col):
        if self.grid2[row][col] == 0:
            return
        if self.grid2[row][col] == 2:
            self.no_two = False
        self.visited.add((row,col))
        for row_val , col_val in self.directions:
            row_d = row_val + row
            col_d = col_val + col

            if self.is_bound(row_d, col_d) and (row_d, col_d) not in self.visited:
                res = self.dfs(row_d , col_d)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and grid1[row][col] == 0 :
                    grid2[row][col] = 2

        self.directions = [(0 ,1) , (0 , -1) ,(1, 0) , (-1, 0)]
        self.grid2 = grid2
        self.visited = set()
        count = 0

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and (row,col) not in self.visited:
                    self.no_two = True 
                    res = self.dfs(row , col)
                    if self.no_two :
                        count += 1
        return count   
