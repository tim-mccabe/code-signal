def arrayPreviousLess(items):
    array = []
    for i in range(0,len(items)):
        pos = -1
        for j in range(0,i):
            if items[j]<items[i]:
                pos = j
        if pos == -1:
            array.append(-1)
        else:
            array.append(items[pos])
    return array