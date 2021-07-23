import re

def solution(dartResult):
    answer = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for c in re.findall('\d+|S|D|T|\*|#', dartResult):
        if c.isdigit(): answer.append(int(c))
        elif c.isalpha(): answer[-1] **= bonus[c]
        elif c == '#': answer[-1] *= -1;
        elif c == '*':
            answer[-1] *= 2
            if len(answer) >= 2: answer[-2] *= 2
    return sum(answer)
