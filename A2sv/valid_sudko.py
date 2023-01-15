class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9,3):
            for col in range(0,9,3):
                values = [1,2,3,4,5,6,7,8,9]
                for row_suduko in range(3):
                    for suduko in range(3):
                        suduko_values = board[row + row_suduko][col + suduko ]

                        if suduko_values != '.':
                            if int(suduko_values) in values:
                                values.remove(int(suduko_values))

                            else:
                                return False

        for row in board:
            values = [1,2,3,4,5,6,7,8,9]
            for col in row:
                if col != '.':
                    if int(col ) in values:
                        values.remove(int(col))
                    else:
                        return False
        for col in range(9):
            values = [1,2,3,4,5,6,7,8,9]
            for rows in board:
                row = rows[col]
                if row != '.':
                    if int(row ) in values:
                        values.remove(int(row))

                    else:
                        return False


        return True