def replaceMiddle(arr):
    l = len(arr)//2
    c = arr[l]
    a = []
    if len(arr) % 2 == 0:
        c += arr[l-1] 
        print(c)
        arr[l-1] = c
        del arr[l]
        return arr
    return arr