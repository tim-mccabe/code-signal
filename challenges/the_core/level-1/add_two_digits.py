def addTwoDigits(n):
    # convert the number to a string so we can iterate through it
    s = str(n)
    # create a counter
    sum_of_digits = 0
    # loop through string
    for digit in s:
        # add each digit to the counter after converting back to integer
        sum_of_digits += int(digit)
    return sum_of_digits

# alternate solution in one line
def addTwoDigits_1(n):
    return n // 10 + n % 10