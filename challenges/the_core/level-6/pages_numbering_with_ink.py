def pagesNumberingWithInk(current, numberOfDigits):
    digets_left = numberOfDigits
    while digets_left >= len(str(current)):
        digets_left -= len(str(current))
        print(digets_left)
        current += 1
    current -= 1
    return current