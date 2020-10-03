def arrayMaximalAdjacentDifference(inputArray):
    m = []
    l = len(inputArray)
    for i in range(1, l):
        m.append(abs(inputArray[i - 1] - inputArray[i]))
    return max(m)    