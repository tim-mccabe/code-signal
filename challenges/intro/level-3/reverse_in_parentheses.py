def reverseInParentheses(inputString):
    # convert the inputString into a list of characters
    chars_list = list(inputString)
    # creat an empty list to hold the indexes of the parentheses
    parentheses_indexes = []
    # loop though and enumerate
    for i, c in enumerate(chars_list):
        #check to see if charcter is an open parentheses "("
        if c == "(":
            # add the index to empty list
            parentheses_indexes.append(i)
        #check to see if charcter is an closed parentheses ")"
        elif c == ")":
            # create a new list without parentheses
            j = parentheses_indexes.pop()
            # reverse what is in the parenthese
            chars_list[j:i] = chars_list[i:j:-1]
    if parentheses_indexes:
        raise ArgumentError("Unclosed parentheseis")
    return "".join(c for c in chars_list if c not in "()")