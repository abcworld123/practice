import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
arr = [[1] * (M + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (M + 2)]
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
ans = 0
q = []

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if arr[i][j]: q.append((i, j))

for i, j in q:
    for dy, dx in d:
        y, x = i + dy, j + dx
        if arr[y][x] == 0:
            arr[y][x] = arr[i][j] + 1
            q.append((y, x))

print(max(max(line) for line in arr) - 1)
