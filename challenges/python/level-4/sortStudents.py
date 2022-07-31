def solution(students):
    students.sort(key=lambda i: i.split()[-1])
    return students
