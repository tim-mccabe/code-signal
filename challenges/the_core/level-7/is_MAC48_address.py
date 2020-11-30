def isMAC48Address(inputString):
    letters = list("ABCDEF")
    x = inputString.split("-")
    l = len(x)
    if l != 6:
        return False
        
    for i in range(l):
        a = x[i]
        l2 = len(a)
        if l2 != 2:
            return False
        for j in range(l2):
            if ((a[j] not in letters) and (a[j].isnumeric()==False)):
                return False
    return True