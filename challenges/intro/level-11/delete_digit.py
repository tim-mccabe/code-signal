def deleteDigit(n):
    l = len(list(str(n)))
    m = 0
    for i in range(l):
        a = list(str(n))
        del a[i]
        num = int(''.join(a))
        if num > m:
            m = num
    return m