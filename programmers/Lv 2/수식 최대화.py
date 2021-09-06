import re
from itertools import permutations

def solution(expr):
    answer = 0
    expr = re.findall('\d+|\D', expr)
    for case in permutations(['+', '-', '*']):
        _expr = expr[:]
        for op in case:
            i = 0
            while i < len(_expr):
                if _expr[i] == op: _expr[i - 1: i + 2] =[str(eval(''.join(_expr[i - 1: i + 2])))]
                else: i += 1
        answer = max(answer, abs(int(_expr[0])))
    return answer
