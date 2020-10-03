def alphabeticShift(inputString):
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = list(alphabet_string)
    l = list(inputString)
    for i in range(len(l)):
        index = [j for j,x in enumerate(alphabet_list) if x == l[i]]
        if index[0] != (len(alphabet_list)-1):
            l[i] = alphabet_list[index[0]+1]
        else:
            l[i] = alphabet_list[0]
    return ''.join(l)