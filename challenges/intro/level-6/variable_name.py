def variableName(name):
    l = list(name)
    for i in range(len(l)):
        if l[0].isnumeric():
            return False
        if not( l[i].isalpha() or l[i].isnumeric() or l[i] == "_"):
            return False
    return True
