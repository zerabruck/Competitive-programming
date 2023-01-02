from collections import Counter
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = {}
        ones_col = {}
        zeros_row = {}
        zeros_col = {}
        result = []

        for row in range(len(grid)):
            ones_sum = sum(grid[row])
            ones_row[row] = ones_sum
            zeros_row[row]= len(grid[row]) - ones_sum
                
        for col in range(len(grid[0])):
            # print(col)
            ones_sum=sum([ i[col] for i in grid ])
            ones_col[col]=ones_sum
            # print(ones_col)
           
            zeros_col[col]=len(grid) - ones_sum
    
        for row in range(len(grid)):
            new_row = []
            for col in range(len(grid[row])):
                value= ones_row[row] + ones_col[col] - zeros_row[row] - zeros_col[col]
                new_row.append(value)

            result.append(new_row)

        return result








            
