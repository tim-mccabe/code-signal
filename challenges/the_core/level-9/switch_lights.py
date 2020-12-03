def switchLights(a):
    boolean_array = []
    for candle in a:
        if candle == 1: boolean_array = reverseValue(boolean_array)
        boolean_array.append(False)
    return convertBooleanInto1and0(boolean_array)
    
def reverseValue(boolean_array):
    return [not boo for boo in boolean_array]
    
def convertBooleanInto1and0(boolean_array):
    return [1 if true else 0 for true in boolean_array]