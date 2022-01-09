import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
arr = [0] + list(map(int, input().split()))
cnt = [0] * 100001
rank = [0] * 100001

M = int(input())
sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(M)]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
s, e, cur = 0, 0, 0

for a, b, i in queries:
    while a < s:
        s -= 1
        cnt[arr[s]] += 1
        x = cnt[arr[s]]
        rank[x - 1] -= 1
        rank[x] += 1
        cur = max(cur, x)
    while e < b:
        e += 1
        cnt[arr[e]] += 1
        x = cnt[arr[e]]
        rank[x - 1] -= 1
        rank[x] += 1
        cur = max(cur, x)
    while s < a:
        x = cnt[arr[s]]
        cnt[arr[s]] -= 1
        rank[x] -= 1
        rank[x - 1] += 1
        if cur == x and rank[x] == 0: cur -= 1
        s += 1
    while b < e:
        x = cnt[arr[e]]
        cnt[arr[e]] -= 1
        rank[x] -= 1
        rank[x - 1] += 1
        if cur == x and rank[x] == 0: cur -= 1
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())



#처음 생각한 방법 (T(N)=lgN)
import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def update(seg, i, v):
    seg[i] += v
    while i > 1023:
        seg[i >> 1] = max(seg[i], seg[i ^ 1])
        i >>= 1

def update2(seg):
    for i in range(9, 0, -1):
        for j in range(1 << i, 1 << (i + 1), 2):
            seg[j >> 1] = max(seg[j], seg[j + 1])


N = int(input())
arr = [0] + list(map(int, input().split()))
seg = [0] * 200000

M = int(input())
sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(M)]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
s, e, n1 = 0, 0, N - 1

for a, b, i in queries:
    while a < s: s -= 1; update(seg, arr[s] + 99999, 1)
    while e < b: e += 1; update(seg, arr[e] + 99999, 1)
    while s < a: update(seg, arr[s] + 99999, -1); s += 1
    while b < e: update(seg, arr[e] + 99999, -1); e -= 1
    update2(seg)
    ans[i] = seg[1]

os.write(1, '\n'.join(map(str, ans)).encode())
