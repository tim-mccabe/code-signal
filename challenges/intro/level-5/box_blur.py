# this function will find the average of the 3 x 3 matrix pixles and be called in boxBlur
def avg_matrix(square):
    #create counter
    t = 0
    # create two loops to get every value in the matrix
    for i in range(3):
        for j in range(3):
            t += square[i][j]
    return t // 9
    
def boxBlur(image):
    # holder for 3 x 3 matrix
    square = []
    # holder for one row of 3 x3 matrix
    square_row = []
    #holder for blurred poixels possible in one row
    blur_row = []
    # holder for blurred image
    blur_img = []
    rows = len(image)
    cols = len(image[0])
    # rp is row pointer and cp is column pointer 
    rp = 0
    cp = 0
    # this while loop will be used to calculate all the blured pixels in the first row
    while rp <= rows - 3:
        while cp <= cols - 3:
            for i in range(rp, rp + 3):
                for j in range(cp, cp + 3):
                    # append all pixels to a row 3 x x matrix
                    square_row.append(image[i][j])
                # append row ro square
                square.append(square_row)
                square_row = []
            # calculate the blured pixle and append to blur_row
            blur_row.append(avg_matrix(square))
            square = []
            # increase column pointer
            cp += 1
        # append blur_row to blur_img
        blur_img.append(blur_row)
        blur_row = []
        # increase the row pointer
        rp += 1
        # start column over
        cp = 0
    return blur_img