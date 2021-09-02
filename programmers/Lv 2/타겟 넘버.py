from itertools import product

def solution(numbers, target):
    arr = [[x, -x] for x in numbers]
    return [sum(x) for x in product(*arr)].count(target)
