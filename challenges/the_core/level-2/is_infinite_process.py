def isInfiniteProcess(a, b):
    if a == b:
        return False
    if (abs(a-b)%2) == 1:
        return True
    if a >= b:
        return True
    return False