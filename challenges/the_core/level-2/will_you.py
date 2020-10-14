def willYou(young, beautiful, loved):
    if young and beautiful and loved:
        return False
    elif young and beautiful and not loved:
        return True
    elif (young and beautiful) or loved:
        return True
    else:
        return False