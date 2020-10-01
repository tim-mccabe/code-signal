def matrixElementsSum(matrix):
    x = len(matrix)
    y = len(matrix[0])
    total = 0
    
    for i in range(y):
        for j in range(x):
            if matrix[j][i] != 0:
                total += matrix[j][i]
            else:
                break
    return total