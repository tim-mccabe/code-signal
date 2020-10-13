def digitsProduct(product):
    a = 4000
    b = 4000
    while True:
        c = 1
        for i in list(str(a)):
            c *= int(i)
        if c == product:
            b = a
        a = a - 1
        if (a == 0) and (b == 4000):
            return -1
        elif a == 0:
            return b