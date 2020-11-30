def isCaseInsensitivePalindrome(inputString):
    inputString = inputString.upper()
    if inputString == inputString[::-1]:
        return True
    return False