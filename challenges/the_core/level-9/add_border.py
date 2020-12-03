def addBorder(picture):
    l = len(picture[0]) + 2
    bordered_matrix = ["*" * l] + [x.center(l,"*") for x in picture] + ["*" * l]
    return bordered_matrix

# alternative solution which may be easier to read 
def addBorder_1(picture): 
    r = ['*'*(len(picture[0])+2)]
    for i in picture:
        r.append('*' + i + '*')
    r.append(r[0])
    return r