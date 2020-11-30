def isTandemRepeat(inputString):
    middle_index = len(inputString) // 2
    if inputString[:middle_index] == inputString[middle_index:]:
        return True
    return False