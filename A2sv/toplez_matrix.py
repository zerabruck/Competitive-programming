class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for index,cols in enumerate(matrix[0]):
            value = matrix[0][index]
            row_ind = 0
            col_ind = index

            while (row_ind <= len(matrix) - 1 and col_ind <= len(matrix[0]) - 1):
                if matrix[row_ind][col_ind] != value:
                    return False

                row_ind += 1
                col_ind += 1


        for index,row in enumerate(matrix[1:]):
            value = matrix[index][0]

            row_ind = index
            col_ind = 0
            while (row_ind <= len(matrix) - 1 and col_ind <= len(matrix[0]) - 1):

                if matrix[row_ind][col_ind] != value:
                    return False

                row_ind += 1
                col_ind += 1

        return True







