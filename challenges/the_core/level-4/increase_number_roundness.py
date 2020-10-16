def increaseNumberRoundness(n):
    is_roundness = False
    is_zero_in_middle = False
    for char in str(n):
        if is_zero_in_middle and char != '0':
            is_roundness = True
        if char == '0':
            is_zero_in_middle = True
    return is_roundness