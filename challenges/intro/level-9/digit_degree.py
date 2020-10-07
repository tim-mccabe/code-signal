def digitDegree(n):
    c = 0
    while True:
        if n >= 10:
            n = sum([int(elem) for elem in str(n)])
            c += 1
        else:
            return c