import sys
from itertools import combinations
input = sys.stdin.readline

def search(arr, remain, q):
    dist = 0
    for i, j, d in q:
        for dy, dx in dir:
            y, x = i + dy, j + dx
            if arr[y][x] <= 2:
                if arr[y][x] == 1:
                    dist += d + 1
                    remain -= 1
                    if remain == 0:
                        return dist
                arr[y][x] = 9
                q.append((y, x, d + 1))


N, M = map(int, input().split())
ori = [[9] * (N + 2)] + [[9] + list(map(int, input().split())) + [9] for _ in range(N)] + [[9] * (N + 2)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
chicken = []
house = 0
ans = 10 ** 9

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ori[i][j] == 1: house += 1
        elif ori[i][j] == 2: chicken.append((i, j, 0))

for q in combinations(chicken, M):
    ret = search([l[:] for l in ori], house, list(q))
    ans = min(ans, ret)

print(ans)
