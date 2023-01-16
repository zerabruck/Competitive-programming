class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []

        for row_indx,row in enumerate(grid[:-2]):
            rows = []
            for col_indx,col in enumerate(row[:-2]):
                max_result = 0
                for i in range(3):
                    for j in range(3):
                        max_result = max(max_result,grid[row_indx + i][col_indx + j])

                rows.append(max_result)
            maxLocal.append(rows)

        return maxLocal


