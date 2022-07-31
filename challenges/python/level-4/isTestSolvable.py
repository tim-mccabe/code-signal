def solution(ids, k):
    digitSum = lambda r: sum(map(int,str(r)))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
