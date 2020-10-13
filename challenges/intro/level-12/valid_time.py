def validTime(time):
    t = time.split(':')
    if (0 <= int(t[0]) < 24) and (0 < int(t[1]) <= 59):
        return True
    return False