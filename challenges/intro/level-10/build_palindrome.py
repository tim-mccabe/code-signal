def buildPalindrome(st):
    l = list(st)
    a = len(l)
    for i in range(a):         
        s = st[i:a]
        if isPalindrome(s):
            n = st[0:i]
            return st + n[::-1]
            
def isPalindrome(s):
    return s == s[::-1]