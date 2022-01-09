import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
comp = {v: i for i, v in enumerate(sorted(set(arr)))}
l = len(comp) - 1
arr = [comp[x] for x in arr]
fw = [0] * (l + 1)
sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(M)]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
s, e, cur, i = 1, 1, 0, arr[1]
while i <= l: fw[i] += 1; i += i & -i

for a, b, i in queries:
    while a < s:
        s -= 1
        x = arr[s]
        r1, v1 = 0, x - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while x <= l: fw[x] += 1; x += x & -x
        cur += r1
    while e < b:
        e += 1
        x = arr[e]
        r1, v1 = 0, l
        r2, v2 = 0, x
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        while x <= l: fw[x] += 1; x += x & -x
        cur += r1 - r2
    while s < a:
        x = arr[s]
        r1, v1 = 0, x - 1
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while x <= l: fw[x] -= 1; x += x & -x
        cur -= r1
        s += 1
    while b < e:
        x = arr[e]
        r1, v1 = 0, l
        r2, v2 = 0, x
        while v1: r1 += fw[v1]; v1 -= v1 & -v1
        while v2: r2 += fw[v2]; v2 -= v2 & -v2
        while x <= l: fw[x] -= 1; x += x & -x
        cur -= r1 - r2
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())
