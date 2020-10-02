def palindromeRearranging(inputString):
    # create a counting variable to check to see how many odd characters appear an odd number of times
    odds = 0
    # turn the input string into a set so we can loop through it
    s = set(inputString)
    # loop through the new set
    for x in s:
        # count the number of times a character appears
        n = inputString.count(x)
        # check to see if it an odd number of times
        if (n % 2 != 0):
            # add 1 to the odds counter
            odds += 1
    return odds <= 1
