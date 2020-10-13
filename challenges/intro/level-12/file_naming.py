def fileNaming(names):
    if len(names) != 0:
        new_names = [names[0]] 
        for i in range(1, len(names[1:])+1):
            if names[i] in new_names:
                a = 1
                while names[i] + '(' + str(a) + ')' in new_names:
                    a += 1
                new_names.append(names[i] + '(' + str(a) + ')')
            else:
                new_names.append(names[i])
        return new_names
    return names