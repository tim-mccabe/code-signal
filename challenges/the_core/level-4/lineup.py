def lineUp(commands):
    s = len(commands)
    a = 0
    degree = 0
    for i in range(0, s):
        if commands[i] == 'L':
            degree += -90
        elif commands[i] == 'R':
            degree += 90 
        elif commands[i] == 'A':
            degree += 180
        if degree % 180 == 0:
            a += 1
            degree = 0
    return a