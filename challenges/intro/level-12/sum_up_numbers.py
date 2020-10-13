def sumUpNumbers(inputString):
    l = list(inputString)
    c = 0
    a = []
    for i in range(len(l)):
        if l[i].isdigit():
            a.append(l[i])
            if i == (len(l)-1):
                c = c + int(''.join(a))
        elif len(a) != 0:
            c = c + int(''.join(a))
            a = []
    return c