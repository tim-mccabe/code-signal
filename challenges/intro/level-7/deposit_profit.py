def depositProfit(deposit, rate, threshold):
    a = False
    r = 1 + (rate / 100)
    y = 0
    # if deposit >= threshold:
    #     return 0
    while a is False:
        b = deposit * (r ** y)
        if b >= threshold:
            a = True
            return y
        else:
            y += 1
