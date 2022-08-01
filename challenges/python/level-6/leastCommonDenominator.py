from math import gcd

def solution(denominators):
    return functools.reduce(lambda a, b: (int(a) * int(b)) / gcd(int(a), int(b)), denominators)