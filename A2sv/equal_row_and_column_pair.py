from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        the idea of the question here is that we must find row and a cloumn 
        that are equal and return the total amount of row and column that are
        equal

        -----------
        i will implement it by first creating a dictionary for a row 
        and dictionary for every column by making the key to be the row or 
        the column and the value to be the reption value of the row or column

        after that i will go through the column and if i find the same keys in the row 
        i will multiply the values of the two and sum it to the total count
        """
        row_dict = Counter([tuple(i) for i in grid])
        col_dict = {}

        for i in range(len(grid[0])):
            col = []
            for row in grid:
                col.append(row[i])

            col=tuple(col)

            if col not in col_dict:
                col_dict[col] = 1

            else:
                col_dict[col] += 1

        count = 0 
        for i in col_dict:
            if i in row_dict:
                value = col_dict[i] * row_dict[i]
                count += value

        
        return count
