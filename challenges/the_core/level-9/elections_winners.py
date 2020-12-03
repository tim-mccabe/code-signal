def electionsWinners(votes, k):
    m = max(votes)
    c = 0
    if k == 0:
        for j in votes:
            if j == m:
                c += 1
        if c == 1:
            return c
        else:
            return 0            
    for i in votes:
        if (i + k) > m:
            c += 1
    return c