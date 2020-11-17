def isSumOfConsecutive2(n):
    c = 0
    l = 1
    while(l * (l + 1) < 2 *n):
        a = (1 * n - (l * (l + 1)) / 2) / (l +1)
        if (a - int(a) == 0):
            c += 1
        l += 1
    return c