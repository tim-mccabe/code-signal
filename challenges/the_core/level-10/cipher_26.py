def cipher26(message):
    l = []
    s = 0
    for i in range(0, len(message)):
        temp = (ord(message[i]) - ord('a') - s + 26) % 26
        s += temp
        l.append(chr(temp + ord('a')))
    return ''.join(l)