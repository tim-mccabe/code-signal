def firstNotRepeatingCharacter(s):
    b = {}
    for i in s:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    for i in b:
        if b[i] == 1:
            return i
    return "_"