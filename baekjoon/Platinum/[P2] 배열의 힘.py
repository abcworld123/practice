import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt = [0] * 1000001

sqrtN = int(N / (M ** .5))
queries = [(*map(int, input().split()), i) for i in range(M)]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
s, e, cur = 0, 0, 0
power = 0
ans = [0] * len(queries)

for a, b, i in queries:
    while a < s:
        s -= 1
        x = arr[s]
        cnt[x] += 1
        power += (2 * cnt[x] - 1) * x
    while e < b:
        e += 1
        x = arr[e]
        cnt[x] += 1
        power += (2 * cnt[x] - 1) * x
    while s < a:
        x = arr[s]
        power -= (2 * cnt[x] - 1) * x
        cnt[x] -= 1
        s += 1
    while b < e:
        x = arr[e]
        power -= (2 * cnt[x] - 1) * x
        cnt[x] -= 1
        e -= 1
    ans[i] = power

os.write(1, '\n'.join(map(str, ans)).encode())
