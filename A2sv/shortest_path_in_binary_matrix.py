class Solution:
    def in_bound(self, row, col , grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        if grid[0][0] == 1:
            return -1

        if len(grid) == 1:
            return 1
        
        layer = 1
        quee = deque([(0,0)])
        visited = set()

        while quee:
            print(quee)
            number = len(quee)

            for _ in range(number):

                val = quee.popleft()
                

                for row , col in directions:
                    row_val = row + val[0]
                    col_val = col + val[1]
                    if self.in_bound(row_val, col_val, grid) and (row_val,col_val) not in visited and grid[row_val][col_val] == 0:
                        visited.add((row_val, col_val))
                        quee.append((row_val,col_val))
                        if (row_val,col_val) == (len(grid) - 1, len(grid) - 1):
                            return layer + 1
            layer += 1

        return -1
