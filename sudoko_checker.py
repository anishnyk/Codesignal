# Function to check a 9x9 grid for a valid sudoko puzzle

def sudoku2(grid):
    # check each row
    for i in range(len(grid)):
        row = set()
        for j in range(len(grid)):
            if grid[i][j] == '.':
                continue
            if grid[i][j] in row:
                return False
            else:
                row.add(grid[i][j])
        print(row)
    
    # check each column
    for j in range(9):
        col = set()
        for i in range(9):
            if grid[i][j] == '.':
                continue
            if grid[i][j] in col:
                return False
            else:
                col.add(grid[i][j])
        print(col)
    
    # check each 3x3 block
    for a in range(0, 7, 3):
        for b in range(0,7,3):
            block = set()
            for i in range(a, a+3):
                for j in range(b, b+3):
                    if grid[i][j] == '.':
                        continue
                    if grid[i][j] in block:
                        return False
                    else:
                        block.add(grid[i][j])
            print(block)
    
    return True
    

    