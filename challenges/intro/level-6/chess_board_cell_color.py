def chessBoardCellColor(cell1, cell2):
    if cell1 == cell2:
        return True
    x = "ABCDEFGH"
    y = "12345678"
    letters = list(x)
    numbers = list(y)
    index_letters = 0
    index_nums = 0
    colors = [0]*2
    color_index = 0
    
    for i in numbers:
        index_nums += 1
        index_letters = 0
        for j in letters:
            # if both indexes of letters and numbers are both odd or both even it means both are the same color
            if (((j + i) == cell1) or ((j + i) == cell2)):
                if(((index_nums % 2 != 0) and (index_letters % 2 != 0)) or ((index_nums % 2 == 0) and (index_letters % 2 == 0))):
                    colors[color_index] = 'black'
                else:
                    colors[color_index] = 'white'
                color_index += 1
                if color_index == 2:
                    if (((colors[0] == 'white') and (colors[1] == 'white')) or ((colors[0] == 'black') and (colors[1] == 'black'))):
                        return True
                    else:
                        return False
            index_letters += 1