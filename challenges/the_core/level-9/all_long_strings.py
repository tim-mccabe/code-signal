def allLongestStrings(inputArray):
    a = 0
    for i in inputArray:
        if len(i) > a:
            a = len(i)
    l = []
    for j in inputArray:
        if len(j) == a:
            l.append(j)
    return l