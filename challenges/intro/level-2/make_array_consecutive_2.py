def makeArrayConsecutive2(statues):
    statues.sort()
    fL = 0
    sL = 1
    last_item = len(statues) - 1
    differences = 0
    
    while (fL <= last_item - 1) and (sL <= last_item):
        if statues[sL] - statues[fL] > 1:
            differences += (statues[sL] - statues[fL] - 1)
        fL += 1
        sL += 1
    return differences