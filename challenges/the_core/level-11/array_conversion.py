def arrayConversion(inputArray):
    k = int(math.log(len(inputArray),2))
    for i in range(0,k):
        new_l = []
        if i % 2 == 0:
            for j in range(0,len(inputArray),2):
                new_l.append(inputArray[j] + inputArray[j+1])
        else:
            for j in range(0,len(inputArray),2):
                new_l.append(inputArray[j] * inputArray[j+1])
        inputArray = new_l
    return inputArray[0]