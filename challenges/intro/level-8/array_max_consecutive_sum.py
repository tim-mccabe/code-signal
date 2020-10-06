def arrayMaxConsecutiveSum(inputArray, k):
    c = sum(inputArray[0:k])
    m = c
    for i in range(k, len(inputArray)):
            c = c - inputArray[i-k] + inputArray[i]
            if c > m:
                m = c
    return m