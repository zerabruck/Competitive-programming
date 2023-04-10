class Solution:
    def isbound(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def find_ones(self , row , col , visited):
        if self.grid[row][col] == 0:
            return 0
        count = 1
        visited.add((row,col))

        for row_indx , col_indx in self.directions:
            row_val = row + row_indx
            col_val = col + col_indx
            if self.isbound(row_val , col_val) and (row_val,col_val) not in visited:
                res = self.find_ones(row_val , col_val , visited)
                count += res
        self.grid[row][col] = 0
        return count

    def find_zeros(self, row , col):
        if (row,col) in self.visited:
            return

        self.visited.add((row,col))
        for row_indx , col_indx in self.directions:
            row_val = row + row_indx
            col_val = col + col_indx
            if self.isbound(row_val , col_val) and self.grid[row_val][col_val] == 1:
                res = self.find_ones(row_val , col_val , set())
                self.max_area = max(self.max_area , res)

            if self.isbound(row_val , col_val):
                self.find_zeros(row_val , col_val)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.directions = [(1, 0) , (-1, 0) , (0, 1) , (0, -1) ,(0 , 0)]
        self.grid = grid
        self.max_area = 0
        self.find_zeros(0 , 0)
        return self.max_area
