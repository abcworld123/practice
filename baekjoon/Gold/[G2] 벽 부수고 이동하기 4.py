import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [[1] * (M + 2)] + [[1] + list(map(int, input().rstrip())) + [1] for _ in range(N)] + [[1] * (M + 2)]
area = [[0] * (M + 2) for _ in range(N + 2)]
ans = [[0] * M for _ in range(N)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur = 2

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j] == 0:
            arr[i][j] = cur
            q = [(i, j)]
            for yy, xx in q:
                for dy, dx in d:
                    y, x = yy + dy, xx + dx
                    if arr[y][x] == 0:
                        arr[y][x] = cur
                        q.append((y, x))
            cur += 1
            l = len(q)
            for y, x in q:
                area[y][x] = l

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j] == 1:
            dup, c = [], 0
            for dy, dx in d:
                y, x = i + dy, j + dx
                if arr[y][x] not in dup:
                    dup.append(arr[y][x])
                    c += area[y][x]
            ans[i - 1][j - 1] = (c + 1) % 10


print('\n'.join(''.join(map(str, line)) for line in ans))
