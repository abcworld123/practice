import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
comp = {v: i for i, v in enumerate(sorted(set(arr)))}
arr = [comp[x] for x in arr]
cnt = [0] * 500001
rank = [0] * 500001

sqrtN = 1500
queries = [(*map(int, input().split()), i) for i in range(M)]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
s, e = 0, 0

for a, b, i in queries:
    while a < s:
        s -= 1
        cnt[arr[s]] += 1
        x = cnt[arr[s]]
        rank[x - 1] -= 1
        rank[x] += 1
    while e < b:
        e += 1
        cnt[arr[e]] += 1
        x = cnt[arr[e]]
        rank[x - 1] -= 1
        rank[x] += 1
    while s < a:
        x = cnt[arr[s]]
        cnt[arr[s]] -= 1
        rank[x] -= 1
        rank[x - 1] += 1
        s += 1
    while b < e:
        x = cnt[arr[e]]
        cnt[arr[e]] -= 1
        rank[x] -= 1
        rank[x - 1] += 1
        e -= 1
    ans[i] = rank[2]

os.write(1, '\n'.join(map(str, ans)).encode())
