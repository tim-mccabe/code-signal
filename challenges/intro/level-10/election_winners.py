def electionsWinners(votes, k):
    a = 0
    for i in range(0,len(votes)):
        newVotes = list(votes)
        newVotes[i] += k
        if newVotes[i] == max(newVotes) and newVotes.count(newVotes[i]) == 1:
            a += 1
    return a