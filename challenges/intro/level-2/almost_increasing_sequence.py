def almostIncreasingSequence(sequence):
    #take out the edge cases
    if len(sequence) <= 2:
        return True
    
    #set up a new function to see if it's increasing sequence
    def increasingSequence(test_sequence):
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]:
                return True
        else:
            for i in range(0, len(test_sequence) - 1):
                if test_sequence[i] >= test_sequence[i + 1]:
                    return False
                else:
                    pass
            return True
            
    for i in range(0, len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            #either remove the current one or the next one
            test_seq1 = sequence[:i] + sequence[i + 1:]
            test_seq2 = sequence[:i+1] + sequence[i + 2:]
            if increasingSequence(test_seq1) == True:
                return True
            elif increasingSequence(test_seq2) == True:
                return True
            else:
                return False

# a much simpler version

def almostIncreasingSequence_1(sequence):
    counter = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
    return ccounter < 3