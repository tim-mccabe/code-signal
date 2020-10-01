def allLongestStrings(inputArray):
    max_len = len(max(inputArray, key = len))
    return [s for s in inputArray if len(s) == max_len]
            