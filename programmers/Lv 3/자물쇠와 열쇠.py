def rotate(key, N):
    return [[key[N - j - 1][i] for j in range(N)] for i in range(N)]

def pp(key):
    arr = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j]: arr.append((i, j))
    return arr

def solution(key, lock):
    N, M = len(key), len(lock)
    _n = sum(l.count(0) for l in lock)
    lock = [[9] * (M + 2 * N - 2)] * (N - 1) + [[9] * (N - 1) + l + [9] * (N - 1) for l in lock] + [[9] * (M + 2 * N - 2)] * (N - 1)

    for _ in range(4):
        arr = pp(key)
        for i in range(N + M - 1):
            for j in range(N + M - 1):
                n = _n
                for y, x in arr:
                    if lock[i + y][j + x] == 1: break
                    elif lock[i + y][j + x] == 0: n -= 1
                if n == 0: return True
        key = rotate(key, N)
    return False
