def squareDigitsSequence(a0):
    a = [a0]
    while a[-1] not in a[:-1]:
        a.append(sum(int(i)**2 for i in str(a[-1])))
    return len(a)