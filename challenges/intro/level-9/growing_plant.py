def growingPlant(upSpeed, downSpeed, desiredHeight):
    s = 0
    d = 0
    while True:
        d += 1
        s += upSpeed
        if desiredHeight <= s:
            return d
        s -= downSpeed
        if desiredHeight <= s:
            return d