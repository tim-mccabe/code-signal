def isBeautifulString(inputString):
    alphabet = list(string.ascii_lowercase)
    l = sorted(list(inputString))
    c = [1]
    w = 0
    if l[0] != 'a':
        return False
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            c[w] += 1
        else:
            indexes = alphabet.index(l[i])
            if alphabet[indexes+1] != l[i+1]:
                return False
            w += 1
            c.append(1)
    for x in range(len(c)-1):
        if c[x] < c[x+1]:
            return False
    return True