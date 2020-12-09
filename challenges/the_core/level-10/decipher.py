def decipher(cipher):
    d = []
    while cipher:
        if cipher[0]=='9':
            d.append(cipher[0:2])
            cipher = cipher[2:]
        else:
            d.append(cipher[0:3])
            cipher = cipher[3:]
    
    for i in range(0,len(d)):
        d[i] = chr(int(d[i]))
    
    return "".join(d)