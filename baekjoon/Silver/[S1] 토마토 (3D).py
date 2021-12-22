import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

M, N, H = map(int, input().split())
arr = [[[-1] * (M + 2)] * (N + 2)]
sq_border = [-1] * (M + 2)
q, total = [], 0

for z in range(1, H + 1):
    sq = [sq_border]
    for y in range(1, N + 1):
        l = [-1] + list(map(int, input().split())) + [-1]
        for x in range(1, M + 1):
            if l[x] >= 0:
                total += 1
                if l[x] == 1: q.append((z, y, x, 0))
        sq.append(l)
    sq.append(sq_border)
    arr.append(sq)
arr.append(arr[0])

for z, y, x, c in q:
    for Z, Y, X in ((z - 1, y, x), (z + 1, y, x), (z, y - 1, x), (z, y + 1, x), (z, y, x - 1), (z, y, x + 1)):
        if arr[Z][Y][X] == 0:
            arr[Z][Y][X] = 1
            q.append((Z, Y, X, c + 1))

print(q[-1][3] if len(q) == total else -1)
