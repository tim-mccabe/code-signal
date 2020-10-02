def addBorder(picture):
    # create a new variable for length by adding 2
    # this will represent new length of the matrix with a "*" on either side
    l = len(picture[0]) + 2
    # create the new matrix by adding a row of "*" of length l to the top
    # center the original matrix in between "*" and finally add a row of "*" to the bottom
    bordered_matrix = ["*" * l] + [x.center(l,"*") for x in picture] + ["*" * l]
    return bordered_matrix

# alternative solution which may be easier to read 
def addBorder_1(picture):
    # create a new matrix r with the first row as all "*" with original length + 2 
    r = ['*'*(len(picture[0])+2)]
    # loop through each row of original matrix
    for i in picture:
        # take each row and add "*" to either side of it and append to new martix r
        r.append('*' + i + '*')
    # append the first row to the bottom of the matrix
    r.append(r[0])
    return r