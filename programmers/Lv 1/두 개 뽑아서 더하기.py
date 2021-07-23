from itertools import combinations

def solution(numbers):
    answer = set()
    for x in combinations(numbers, 2):
        answer.add(sum(x))
    return sorted(list(answer))
