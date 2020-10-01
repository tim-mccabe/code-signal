def isLucky(n):
    # convert n to s string
    s = str(n)
    # find the first half of the new string and convert it to a list
    first_half = sum([int(x) for x in list(s[0:int(len(s) / 2)])])
    # repeat for seconf half
    second_half = sum([int(x) for x in list(s[int(len(s) / 2):len(s)])])
    return first_half == second_half
