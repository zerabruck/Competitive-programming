class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        result=0

        for i in range(len(grid)-2):
            for j in range(1,len(grid[i])-1):
                
                clock_value=grid[i][j-1] + grid[i][j]+grid[i][j+1]+grid[i+1][j]+grid[i+2][j-1]+grid[i+2][j]+grid[i+2][j+1]
                
                result=max(result,clock_value)

               

                


        return result