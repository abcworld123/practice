import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = [[0] * (N + 2) for _ in range(N + 2)]
ans = 0

for i in range(2, 3 * M + 2, 3):
    a, b, x = map(int, input().split())
    arr[a][b] = max(arr[a][b], x + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if arr[i][j]:
            ans += 1
            arr[i + 1][j] = max(arr[i][j] - 1, arr[i + 1][j])
            arr[i + 1][j + 1] = max(arr[i][j] - 1, arr[i + 1][j + 1])

print(ans)
