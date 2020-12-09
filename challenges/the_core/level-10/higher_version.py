def higherVersion(ver1, ver2):
    s1 = ver1.split('.')
    s2 = ver2.split('.')
    for i in range(0,len(s1)):
        if int(s1[i])>int(s2[i]):
            return True
        elif int(s1[i])<int(s2[i]):
            return False    
    return False