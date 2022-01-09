import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
fw = [0] * 100001
sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(int(input()))]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
s, e, cur, i = 1, 1, 0, arr[1]
while i <= 100000: fw[i] += 1; i += i & -i

for a, b, i in queries:
    while a < s:
        s -= 1
        x = arr[s]
        r1, v1 = 0, 100000 if 100000 < x + K else x + K
        r2, v2 = 0, 0 if 0 > x - K - 1 else x - K - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        cur += r1 - r2
        while x <= 100000: fw[x] += 1; x += x & -x
    while e < b:
        e += 1
        x = arr[e]
        r1, v1 = 0, 100000 if 100000 < x + K else x + K
        r2, v2 = 0, 0 if 0 > x - K - 1 else x - K - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        cur += r1 - r2
        while x <= 100000: fw[x] += 1; x += x & -x
    while s < a:
        x, _x = arr[s], arr[s]
        while _x <= 100000: fw[_x] -= 1; _x += _x & -_x
        r1, v1 = 0, 100000 if 100000 < x + K else x + K
        r2, v2 = 0, 0 if 0 > x - K - 1 else x - K - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        cur -= r1 - r2
        s += 1
    while b < e:
        x, _x = arr[e], arr[e]
        while _x <= 100000: fw[_x] -= 1; _x += _x & -_x
        r1, v1 = 0, 100000 if 100000 < x + K else x + K
        r2, v2 = 0, 0 if 0 > x - K - 1 else x - K - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        cur -= r1 - r2
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())
