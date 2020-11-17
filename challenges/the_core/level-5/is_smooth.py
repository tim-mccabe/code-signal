def isSmooth(arr):
    l = len(arr)//2
    print(l)
    a = arr[0]
    b = arr[-1]
    c = arr[l]
    if len(arr) % 2 == 0:
        c += arr[l-1] 
    if a == b and b == c:
        return True
    return False