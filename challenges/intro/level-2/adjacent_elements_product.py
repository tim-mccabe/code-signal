def adjacentElementsProduct(inputArray):
    return max(a * b for a, b in zip(inputArray, inputArray[1:]))

# alternative solution

def adjacentElementsProduct_1(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])