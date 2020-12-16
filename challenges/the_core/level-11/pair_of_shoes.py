def pairOfShoes(shoes):
    if shoes==[] or len(shoes)%2!=0:
        return False
    while shoes!=[]:
        shoe = shoes[0]
        if [1-shoe[0],shoe[1]] not in shoes:
            return False
        else:
            shoes = shoes[1:]
            i = 0
            while shoes[i] != [1-shoe[0],shoe[1]]:
                i += 1
            shoes =shoes[0:i]+shoes[i+1:]
    
    return True