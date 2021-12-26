import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
arr = [0] + list(map(int, input().split()))
cnt = [0] * 1000001

sqrtN = 1000
queries = [(*map(int, input().split()), i) for i in range(int(input()))]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
s, e, cur = 0, 0, 0
ans = [0] * len(queries)

for a, b, i in queries:
    while a < s:
        s -= 1
        cnt[arr[s]] += 1
        if cnt[arr[s]] == 1: cur += 1
    while e < b:
        e += 1
        cnt[arr[e]] += 1
        if cnt[arr[e]] == 1: cur += 1
    while s < a:
        cnt[arr[s]] -= 1
        if cnt[arr[s]] == 0: cur -= 1
        s += 1
    while b < e:
        cnt[arr[e]] -= 1
        if cnt[arr[e]] == 0: cur -= 1
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())
