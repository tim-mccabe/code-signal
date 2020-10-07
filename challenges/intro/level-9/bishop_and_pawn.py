def bishopAndPawn(bishop, pawn):
    letters = ["a","b","c","d","e","f","g","h"]
    numbers = ["1","2","3","4","5","6","7","8"]
    
    b = list(bishop)
    p = list(pawn)
    
    for i in range(len(letters)):
        if b[0] == letters[i]:
            idx_b = i
        if p[0] == letters[i]:
            idx_p = i
    x = abs(idx_b-idx_p)
    
    if (int(b[1]) == (int(p[1]) - x)) or (int(b[1]) == (int(p[1]) + x)):
        return True
    else:
        return False 