import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for T in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * (M + 2) for _ in range(N + 2)]
    for _ in range(K):
        y, x = input().split()
        arr[int(x) + 1][int(y) + 1] = 1
    ans = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j]:
                ans += 1
                arr[i][j] = 0
                q = [(i, j)]
                for x, y in q:
                    if arr[x][y - 1]: q.append((x, y - 1)); arr[x][y - 1] = 0
                    if arr[x][y + 1]: q.append((x, y + 1)); arr[x][y + 1] = 0
                    if arr[x - 1][y]: q.append((x - 1, y)); arr[x - 1][y] = 0
                    if arr[x + 1][y]: q.append((x + 1, y)); arr[x + 1][y] = 0
    print(ans)
