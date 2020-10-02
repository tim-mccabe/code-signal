def candies(n, m):
    # find how many will not be eaten by finding the remainder of candy / kids
    left_overs = m % n
    # subtract leftovers from m to find out total candy eaten
    return m - left_overs