def differentSquares(matrix):
    allCoordinates = findTopLeftCoordinateOfSquare(matrix)
    aSet = set()
    for coordi in allCoordinates:
        aSet.add(turnSquareToString(matrix, coordi[0], coordi[1]))
    return len(aSet)
    
def findTopLeftCoordinateOfSquare(matrix):
    results = []
    deep = len(matrix)
    wide = len(matrix[0])
    for i in range(0, deep - 1):
        for j in range(0, wide - 1):
            results.append([i,j])
    return results

def turnSquareToString(matrix, deep, wide):
    string = str(matrix[deep][wide])
    string += str(matrix[deep + 1][wide + 1])
    string += str(matrix[deep + 1][wide])
    string += str(matrix[deep][wide + 1])
    return string