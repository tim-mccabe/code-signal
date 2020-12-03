def areSimilar(a, b):
    # run the function potentialSwaps
    # the variable pair will be an array of the indexes of different values in aray a an b
    pair = potentialSwaps(a, b)
    # check to see if a and b arrays are exactly the same; if the array is empty there is no need to swap anything
    if len(pair) == 0:
        return True
    # check to see if two are able to swap
    if len(pair) == 2:
        # swap the pairs
        swap(a, pair[0], pair[1])
        # run the potentialSwaps function again
        pair = potentialSwaps(a, b)
        # if there are no new pairs then return ture
        return len(pair) == 0
    # if potential swaps still remain return false
    return False

# create a fucntion you can call to look for potential swaps
def potentialSwaps(a, b):
    # create an empty list to hold the pair able to swap
    s = []
    # loop through the length of the first array a
    for x in range(len(a)):
        # check for potential to swap
        if (a[x] != b[x]):
            # add to empty list if not
            s.append(x)
    return s
    
# create a function to swap
def swap(array, index_1, index_2):
    array[index_1], array[index_2] = array[index_2], array[index_1]