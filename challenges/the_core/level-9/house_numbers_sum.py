def houseNumbersSum(inputArray):
    c = 0
    for i in inputArray:
        c += i
        if i == 0:
            break
    return c
