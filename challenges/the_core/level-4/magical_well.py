def magicalWell(a, b, n):
    c = 1
    d = 0
    while c <= n:
        d += (a * b)
        a += 1
        b += 1
        c += 1
    return d