def seatsInTheater(nCols, nRows, col, row):
    # find how many columns are to your left (including your own)
    c = nCols - (col - 1)
    # find how many rows behind you
    r = nRows - row
    return c * r
