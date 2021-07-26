c = -1
def solution(num):
    global c
    c += 1
    return solution(num // 2 if num & 1 == 0 else num * 3 + 1) if num != 1 else c if c <= 500 else -1
