import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
ans = []

for y in range(1, N + 1):
    for x in range(2, N + 1):
        arr[y][x] += arr[y][x - 1]

for x in range(1, N + 1):
    for y in range(2, N + 1):
        arr[y][x] += arr[y - 1][x]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])

sys.stdout.write('\n'.join(map(str, ans)))
