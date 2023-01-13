class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if row[0] <= target <= row[-1]:
                for col in row:
                    if col == target:
                        return True

                    elif col > target:
                        return False

            elif row[0] > target :
                return False

        