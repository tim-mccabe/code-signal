def minimalNumberOfCoins(coins, price):
    c = -1
    n = 0
    while price > 0 and abs(c) <= len(coins):
        if price >= coins[c]:
            price -= coins[c]
            n += 1
        else:
            c -= 1
    return n