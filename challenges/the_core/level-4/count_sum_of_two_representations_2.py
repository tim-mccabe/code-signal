def countSumOfTwoRepresentations2(n, l, r):
    c = 0
    if l <= n//2 <= r:
        if n % 2 == 0:
            return min([(n//2-l)+1,(r-n//2)+1])
        else:
            return min([(n//2-l),(r-n//2)])
    else:
        return 0