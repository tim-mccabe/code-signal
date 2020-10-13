def messageFromBinaryCode(code):
    l = list(code)
    longitude = len(l)
    a = int(longitude/8)
    b = 8
    word = []
    for i in range(a):
        new_word = l[(i*b):(i*b+8)]
        decimal = sum([int(new_word[j])*2**(7-j) for j in range(0,8)])
        word.append(chr(decimal))
    return ''.join(word)