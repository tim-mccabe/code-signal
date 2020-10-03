def neighbors(matrix, i, j, row, col):
    mine = 0
    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine += 1       
    if not (i < 1):
        if matrix[i - 1][j]:
            mine += 1
    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine += 1
    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine += 1
    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine += 1
    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine += 1
    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine += 1
    if not (j < 1):
        if matrix[i][j - 1]:
            mine += 1
    return mine
    
def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sol = []
    for i in range(0, row):
        t = []
        for j in range(0, col):
            t.append(neighbors(matrix, i, j, row, col))
        sol.append(t)
    return sol
