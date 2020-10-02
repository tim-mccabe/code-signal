def phoneCall(min1, min2_10, min11, s):
    m = 0    
    if s >= min1:
        m += 1
        s -= min1
    else:
        return m
    for i in range(0,9):
        if s >= min2_10:
            m += 1
            s -= min2_10
    if m == 10:
        while s >= min11:
            m += 1
            s -= min11
    return m

# alternative and shorter solution

def phoneCall_1(min1, min2_10, min11, s):
    if s < min1:
        return 0
    for i in range(2, 11):
        if s < min1 + min2_10 * (i - 1):
            return i - 1
    return (s - min1 - min2_10 * 9.0) //min11 + 10