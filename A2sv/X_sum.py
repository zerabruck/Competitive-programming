loop = int(input())



for i in range(loop):
    grid_size = list(map(int,input().split()))
    rows = grid_size[0]
    #  list(map(int, input().split()))
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
            

            while(initial_row >= 0 or inital_col >= 0):
                initial_row -= 1
                inital_col -= 1

            inital_col += 1
            initial_row += 1

            while(initial_row < rows or inital_col < cols):
                print (initial_row)
                print(inital_col)
                added_val += grid [initial_row][inital_col]
                inital_col += 1
                initial_row += 1

            # -------------------------up to find second diagonal------
            initial_row = row_idx
            inital_col = col_idx
            while(initial_row >= 0 or inital_col < cols):
                initial_row -= 1
                inital_col += 1

            inital_col -= 1
            initial_row += 1

            while(initial_row < rows or inital_col >= 0):
                added_val += grid [initial_row][inital_col]
                inital_col -= 1
                initial_row += 1

            result = max(result,added_val)

    print(result)
                



            





            

            

    print(result)


