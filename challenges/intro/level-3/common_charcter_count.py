def commonCharacterCount(s1, s2):
    # set a counter for common characters in each string
    output = 0
    # convert each string to alist containing on character for each item in list
    s1_list = list(s1)
    s2_list = list(s2)
    # iterate through the first list
    for i in s1_list:
        # iterate through the second list
        for j in s2_list:
            # check to see if the character exists in the second list
            if i == j:
                # add 1 to the counter for each character in common
                output += 1
                # delete the common character from the second list
                s2_list.remove(j)
                break
    #return the counter variable
    return output