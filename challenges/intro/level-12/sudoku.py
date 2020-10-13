def sudoku(grid):
    d1 = []
    d2 = []
    for i in range(0, 9):
        if len(set(grid[i])) != 9:
            return False
        if len(set([row[i] for row in grid])) != 9:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
            if len(set(box)) != 9:
                return False
    return True