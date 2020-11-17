def isPower(n):
    for i in range(21):
        for j in range(2,10):
            if (i ** j) == n:
                return True
    return False
