def reflectString(inputString):
    alpabet = list("abcdefghijklmnopqrstuvwxyz")
    r = alpabet[::-1]
    l = []
    for i in list(inputString):
        c = alpabet.index(i)
        l.append(r[c])
    return ''.join(l)