class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    for new_row in range(len(matrix)):
                        if matrix[new_row][col] == 0:
                            continue
                        else:
                            matrix [new_row][col] = 2**31

                    for new_col in range(len(matrix[0])):
                        if matrix[row][new_col] == 0:
                            continue
                        else:
                            matrix [row][new_col] = 2**31
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 2**31:
                    matrix[row][col] = 0


        

                    

                    
