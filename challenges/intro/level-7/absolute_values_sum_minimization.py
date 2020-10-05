def minima(x,b):
    return sum([abs(elem - x) for elem in b])
    
def absoluteValuesSumMinimization(a):
    l = len(a)
    mid = l/2
    
    if l % 2 == 0:
        return int(a[int(mid - 1)])
    else:
        return int(a[int(mid)])
