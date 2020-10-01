# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# A ticket number represented as a positive integer with an even number of digits.

# Guaranteed constraints:
# 10 ≤ n < 106.

# [output] boolean

# true if n is a lucky ticket number, false otherwise.

def isLucky(n):
    # convert n to s string
    s = str(n)
    # find the first half of the new string and convert it to a list
    first_half = sum([int(x) for x in list(s[0:int(len(s) / 2)])])
    # repeat for seconf half
    second_half = sum([int(x) for x in list(s[int(len(s) / 2):len(s)])])
    return first_half == second_half
