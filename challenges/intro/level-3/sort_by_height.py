def sortByHeight(a):
    # find numbers that are not -1 and sort them
    holder = [x for x in a if x != -1]
    # sort the holder list
    sorted_list = sorted(holder)
    # creat a counter for variable j in order to replace idexed numbers when looping through and replacing
    j = 0
    # loop through original input list and replace any number that is not -1 with one from the sorted_list
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_list[j]
            # add 1 to j to make sure the indexes line up correctly with the sorted_list
            j += 1
    return a