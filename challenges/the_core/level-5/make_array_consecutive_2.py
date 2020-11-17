def makeArrayConsecutive2(statues):
    a = min(statues)
    b = max(statues)
    c = 0
    for i in range(a, b):
        if i not in statues:
            c +=1
    return c