def arrayChange(inputArray):
    # create a counting variable for number of moves it would take to obtain an increasing sequence
    r = 0
    # set a variable for starting point of array
    s = inputArray[0]
    # loop through the length of the array
    for x in inputArray[1:]:
        # compare consecutive numbers 
        if x <= s:
            # find the difference between the two numbers and add 1
            r += (s - x  + 1)
            # add 1 to s to keep it increasing by 1 each time
            s += 1
        # if x is greater set the new s variable to x and continue from there
        else:
            s = x
    return r