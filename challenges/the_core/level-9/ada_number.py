def adaNumber(line):
    line = line.replace("_","")
    
    if "#" not in line:
        return line.isdigit()
    elif line.count("#")!=2:
        return False
    
    line = line.split("#")
    if not line[0].isdigit():
        return False
    elif int(line[0])<2 or int(line[0])>16:
        return False
    
    if line[1]=='':
        return False
    
    for i in range(2,11):
        if int(line[0])==i:
            for j in range(0,len(line[1])):
                if not '0'<=line[1][j]<=str(i-1):
                    return False
                
    for i in range(11,17):
        if int(line[0])==i:
            for j in range(0,len(line[1])):
                if not ('0'<=line[1][j]<='9' or 'a'<=line[1][j]<=chr(i-11+ord('a')) or 'A'<=line[1][j]<=chr(i-11+ord('A'))):
                    return False 

    return True
