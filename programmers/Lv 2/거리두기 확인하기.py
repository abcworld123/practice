import re

def solution(places):
    answer = []
    for place in places:
        lines = [''.join([place[i][j + k] for k in range(3)]) for i in range(5) for j in range(3)]
        lines += [''.join([place[j + k][i] for k in range(3)]) for i in range(5) for j in range(3)]
        squares = [''.join([place[i][j], place[i][j + 1], place[i + 1][j], place[i + 1][j + 1]]) for i in range(4) for j in range(4)]
        if any([re.search('PP|POP', line) for line in lines]): answer.append(0)
        elif any([re.search('POOP|POXP|PXOP|OPPO|OPPX|XPPO', square) for square in squares]): answer.append(0)
        else: answer.append(1)
    return answer
