def alphabetSubsequence(s):
    c = 0
    for i in list(s):
        if ord(i) <= c:
            return False
        else:
            c = ord(i)
    return True