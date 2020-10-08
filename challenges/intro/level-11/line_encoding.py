def lineEncoding(s):
    l = list(s)
    c = 1
    output = ''
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            if c != 1:
                output += str(c) + l[i]
            else:
                output += l[i]
            if i == len(l)-2:
                output += l[i+1]
            c = 1
        else:
            c += 1
            if i == len(l)-2:
                if c != 1:
                    output += str(c) + l[i]
                else:
                    output += l[i]
    return output