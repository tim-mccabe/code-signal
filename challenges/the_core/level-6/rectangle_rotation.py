def rectangleRotation(a, b):
    pt = 0
    radius = pow(a/2,2)+pow(b/2,2)
    radius = int(math.ceil(pow(radius,.5)))
    
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            x = i*math.cos(math.radians(-45)) - j*math.sin(math.radians(-45))
            y = i*math.sin(math.radians(-45)) + j*math.cos(math.radians(-45))
            if -a/2<=x<=a/2 and -b/2<=y<=b/2:
                pt += 1
    return pt