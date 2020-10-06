def extractEachKth(inputArray, k):
    for i in range(len(inputArray)-1, -1, -1):
        if i % k == k - 1:
            del inputArray[i]
    return inputArray