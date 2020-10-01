def checkPalindrome(inputString):
    #reverse string
    rev_string = reversed(inputString)
    
    #check to see if reversed string equals inputString
    if list(inputString) == list(rev_string):
        return True
    else:
        return False
