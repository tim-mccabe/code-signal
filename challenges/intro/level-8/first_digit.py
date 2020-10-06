def firstDigit(inputString):
    for i, c in enumerate(inputString):
        if c.isdigit():
            return(c)
            break
