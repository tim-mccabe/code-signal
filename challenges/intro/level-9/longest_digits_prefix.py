def longestDigitsPrefix(inputString):
    for i in range(len(inputString)):
        if not inputString[i].isnumeric():
            return inputString[0:i]
    return inputString