def houseOfCats(legs):
    l = []
    p = 0
    while legs >= 0:
        if legs % 4 == 2 or legs % 4 == 0:
            c = 1 if (legs % 4) == 2 else 0
        l.append(p + c)
        p += 2
        legs -= 4
    return l