# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s1

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s1.length < 15.

# [input] string s2

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s2.length < 15.

# [output] integer

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