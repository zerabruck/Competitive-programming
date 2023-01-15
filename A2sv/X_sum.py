loop = int(input())
for i in range(loop):
    grid_size = list(map(int,input().split()))
    rows = grid_size[0]
    cols = grid_size[1]

    grid = []
    for i in range(rows):
        row_val = list(map(int,input().split()))
        grid.append(row_val)
    

    result = 0
    
    for row_idx in range(rows):
        for col_idx in range(cols):
            added_val = 0
            # ---------------up to find first diagonal----------
            initial_row = row_idx
            inital_col = col_idx
            

            while(initial_row > 0 and inital_col > 0):
                initial_row -= 1
                inital_col -= 1

            while(initial_row < rows and inital_col < cols):
                added_val += grid [initial_row][inital_col]
                inital_col += 1
                initial_row += 1

            # -------------------------up to find second diagonal------
            initial_row = row_idx
            inital_col = col_idx
            while(initial_row > 0 and  inital_col < cols - 1):
                initial_row -= 1
                inital_col += 1


            while(initial_row < rows  and inital_col >= 0):
                added_val += grid [initial_row][inital_col]
                inital_col -= 1
                initial_row += 1

            result = max(result,added_val - grid[row_idx][col_idx])

    print(result)
                
