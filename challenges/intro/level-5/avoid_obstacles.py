def avoidObstacles(inputArray):
    s = sorted(inputArray)
    j = 1
    obstacle_hit = True
    while(obstacle_hit):
        obstacle_hit = False
        j += 1
        for i in range(0, len(s)):
            if s[i] % j == 0:
                obstacle_hit = True
                break
    return j