# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# reverseInParentheses(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# reverseInParentheses(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# reverseInParentheses(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# reverseInParentheses(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

# Guaranteed constraints:
# 0 ≤ inputString.length ≤ 50.

# [output] string

# Return inputString, with all the characters that were in parentheses reversed.

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