def concatenateArrays(a, b):
    c = []
    for i in range(0,(len(a))):
        c.append(a[i])
    for j in range(0,(len(b))):
        c.append(b[j])
    return c