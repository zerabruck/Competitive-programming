class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        
        magic_squares = 0

        for row_indx,row in enumerate(grid[:-2]):
            
            for col_indx,col in enumerate(row[:-2]):
                values = [1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    for j in range(3):
                        elements =grid[row_indx + i][col_indx + j]
                        if elements in values:
                            values.remove(elements)
                if len(values) != 0:
                    continue 
                first_col = sum([grid[row_indx][col_indx],grid[row_indx + 1][col_indx],grid[row_indx + 2][col_indx]])
                sec_col = sum([grid[row_indx][col_indx + 1],grid[row_indx + 1][col_indx + 1],grid[row_indx + 2][col_indx +1]])
                thrid_col = sum([grid[row_indx][col_indx + 2],grid[row_indx + 1][col_indx + 2],grid[row_indx + 2][col_indx +2]])

                
                first_row = sum([grid[row_indx][col_indx],grid[row_indx][col_indx + 1],grid[row_indx][col_indx + 2]])
                sec_row = sum([grid[row_indx + 1][col_indx],grid[row_indx + 1][col_indx + 1],grid[row_indx + 1][col_indx + 2]])
                thrid_row = sum([grid[row_indx + 2][col_indx ],grid[row_indx + 2][col_indx + 1],grid[row_indx + 2][col_indx +2]])

                first_diagonal = sum ([grid[row_indx][col_indx],grid[row_indx + 1][col_indx + 1],grid[row_indx+ 2][col_indx + 2]])
                second_diagonal = sum ([grid[row_indx][col_indx + 2],grid[row_indx + 1][col_indx + 1],grid[row_indx+ 2][col_indx ]])

                if first_col == sec_col == thrid_col == first_row == sec_row == thrid_row ==first_diagonal == second_diagonal:
                    magic_squares += 1


        return magic_squares
