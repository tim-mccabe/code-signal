def solution(n):
    return [[0] * (n - abs(-i)) for i in range((-n + 1),n)]
