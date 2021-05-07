def solution(v):
    count = 0
    correct = True
    for i in range(len(v)):
        if v[i] == '(': count += 1
        elif v[i] == ')': count -= 1
        if count < 0: correct = False
        elif count == 0:
            if correct: return v[:i + 1] + solution(v[i + 1:])
            else: return '(' + solution(v[i + 1:]) + ')' + v[1: i].replace('(', '_').replace(')', '(').replace('_', ')')
    return v
