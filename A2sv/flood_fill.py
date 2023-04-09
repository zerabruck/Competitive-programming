class Solution:
    def is_bound(self, row , col):
        return 0 <= row < len(self.image) and 0 <= col < len(self.image[0])

    def dfs(self, row , col):
        if self.visited[row][col] == 1:
            return 

        self.visited[row][col] = 1
        for row_val , col_val in self.directions:
            curr_row = row + row_val
            curr_col = col + col_val

            if self.is_bound(curr_row , curr_col) and self.image[curr_row][curr_col] == self.image[row][col]:
                self.dfs(curr_row , curr_col)
        self.image[row][col] = self.color
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.visited = [ [0 for i in range(len(image[0]))] for i in range(len(image)) ]
        self.directions = [(1, 0) , (-1 , 0) , (0, 1) , (0 , -1)]
        self.image = image
        self.color = color
        self.dfs(sr , sc)
        return self.image
