# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more 
# than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is
# also considered to be strictly increasing.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer sequence

# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -105 ≤ sequence[i] ≤ 105.

# [output] boolean

# Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

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