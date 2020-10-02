def firstDuplicate(a):
    num_set = set()
    for i in range(len(a)):
        if a[i] in num_set:
            return a[i]
        else:
            num_set.add(a[i])
    return -1