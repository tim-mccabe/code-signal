def solution(word):
    num = dict(zip(list(string.ascii_lowercase), range(1,27)))
    return sum([num[ch] for ch in word])
