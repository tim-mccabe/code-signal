def additionWithoutCarrying(param1, param2):
    a = str(param1)
    b = str(param2)
    l = ''
    s = ''
    if len(a) >= len(b):
        l = a[::-1]
        s = b[::-1]
    else:
        l = b[::-1]
        s = a[::-1]
    
    results = ''
    count = 0
    
    for char in l:
        if count >= len(s):
            results += char
        else:
            num = int(char) + int(s[count])
            count += 1
            if num > 9:
                results += str(num - 10)
            else:
                results += str(num)
    return int(results[::-1])