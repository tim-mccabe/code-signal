from collections import defaultdict

def digitSum(x):
    return sum(map(int, str(x)[::]))
    
def comfortableNumbers(l, r):
    comfortable = defaultdict(int)
    for a in range(l, r + 1):
        offset = digitSum(a)
        for b in range(a - offset, a + offset + 1):
            if a != b and b in range(l, r + 1):
                if a < b :
                    comfortable[(a, b)] += 1
                else:
                    comfortable[(b, a)] += 1
    count = 0
    for c in comfortable:
        if comfortable[c] == 2:
            count += 1
    return count