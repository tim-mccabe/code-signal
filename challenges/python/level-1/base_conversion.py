def baseConversion(n, x):
    return hex(int(n, x))[2:] # [2:] is for removing the hex prefix 0x