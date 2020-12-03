def characterParity(symbol):
    if symbol.isnumeric() == True:
        if (int(symbol) % 2) == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'not a digit'
