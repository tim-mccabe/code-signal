def alternatingSums(a):
    # create two empty list to hold team 1 and team 2
    team_1 = []
    team_2 = []
    # loop through the length of the given array
    for x in range(len(a)):
        # check to see if the index is divisable by 2
        if(x % 2 != 1):
            # if so, append that to team_1 list
            team_1.append(a[x])
        # if not append to team_2
        else:
            team_2.append(a[x])
    # create a new list of output which are the sums of team_1 and team_2
    output = [sum(team_1), sum(team_2)]
    return output