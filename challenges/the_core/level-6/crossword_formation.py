import itertools

def crosswordFormation(words):
    r = 0
    for w in itertools.permutations(words):
        for s1 in range(len(w[0]) - 2):
            ps1 = [i for i, c in enumerate(w[1]) if c == w[0][s1]]
            for s2 in range(s1 + 2, len(w[0])):
                ps2 = [i for i, c in enumerate(w[2]) if c == w[0][s2]]
                for pw1 in ps1:
                    for pw2 in ps2:
                        for c1, c2 in zip(w[1][pw1 + 2:], w[2][pw2 + 2:]):
                            for c3, c4 in zip(w[3], w[3][s2 - s1:]):
                                r += c1 == c3 and c2 == c4
    return r
