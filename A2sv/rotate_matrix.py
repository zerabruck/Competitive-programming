class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        count = 0

        for row_indx,row in enumerate(matrix):
            for col_indx in range(row_indx,len(row)):
                matrix[row_indx][col_indx] , matrix[col_indx][row_indx] = matrix[col_indx][row_indx] , matrix[row_indx][col_indx]


        for row in matrix:
            row.reverse()

        