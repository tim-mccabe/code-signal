letters = ['*','*','a','b','c','d','e','f','g','h','*','*']
numbers = ['-2','-1','0','1','2','3','4','5','6','7','8','9','10','11']

def move(i, j, l):
    index_letters = letters.index(l[0])
    index_numbers = numbers.index(l[1])
    if (((index_letters+i)>=2) and (index_letters+i<=9)) and ((index_numbers+j>=3) and (index_numbers+j<=10)):
        return ''.join(letters[index_letters+i]+numbers[index_numbers+j])
          
def chessKnight(cell):
    a = []
    l = list(cell)
    for i in [-2,-1,1,2]:
        if abs(i) > 1:
            for j in [-1,1]:
                if not move(i,j,l) is None:
                    a.append(move(i,j,l))
        else:
            for j in [-2,2]:
                if not move(i,j,l) is None:
                    a.append(move(i,j,l))
    return len(a)