import itertools

def stringsRearrangement(inputArray):
    p = itertools.permutations(inputArray)
    for permu in p:
        all_match = True
        for i in range(len(permu) - 1):
            if not isDifferByOneChar(permu[i], permu[i + 1]):
                all_match = False
                break
        if all_match:
            return True
    return False
        
def isDifferByOneChar(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count == 1