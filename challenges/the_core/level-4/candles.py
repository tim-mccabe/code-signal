def candles(candlesNumber, makeNew):
    total_burned = 0
    leftovers = 0
    while candlesNumber > 0:
        total_burned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = 0
        candlesNumber = leftovers // makeNew
        leftovers = leftovers % makeNew
    return total_burned