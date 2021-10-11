answer = []

def hanoi(n, _from, _mid, _to):
    if n == 1: answer.append([_from, _to]); return
    hanoi(n - 1, _from, _to, _mid)
    answer.append([_from, _to])
    hanoi(n - 1, _mid, _from, _to)

def solution(n):
    hanoi(n, *range(1, 4))
    return answer
