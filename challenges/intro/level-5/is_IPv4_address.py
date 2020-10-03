def isIPv4Address(inputString):
    l = list(inputString.split("."))
    print(l)
    for x in l:
        if len(x) > 1 and x.startswith("0"):
            return False
    return len(l) == 4 and all(i.isdigit() and 0 <= int(i) <= 255 for i in l)

# alternative solution

def isIPv4Address_1(inputString):
    l = list(inputString.split("."))
    print(l)
    if "" in l or len(l) != 4:
        return False
    for x in l:
        if len(x) > 1 and x.startswith("0"):
            return False
    try:
        for i in l:
            if not 0 <= int(i) <= 255:
                return False
    except ValueError:
        return False
    except TypeError:
        return False
    return True