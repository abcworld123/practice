import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


N, K = map(int, input().split())
arr = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
fq, bq = [], []
remain, day = K, 0

for _ in range(K):
    y, x = map(int, input().split())
    bq.append((y, x))
    arr[y][x] = 2

fq.append((bq[0][0], bq[0][1]))
arr[fq[0][0]][fq[0][1]] = 1
remain -= 1

while bq:
    new_fq, new_bq = [], []
    for i, j in fq:
        flag = 0
        for dy, dx in d:
            y, x = i + dy, j + dx
            if arr[y][x] & 2:
                if arr[y][x] == 2: remain -= 1
                arr[y][x] = 1
                fq.append((y, x))
            elif arr[y][x] == 0 and not flag:
                new_fq.append((i, j))
                flag = 1
    if remain == 0: break

    for i, j in bq:
        for dy, dx in d:
            y, x = i + dy, j + dx
            if arr[y][x] == 0:
                arr[y][x] = 6
                new_bq.append((y, x))
    fq = new_fq
    bq = new_bq
    day += 1

print(day)
