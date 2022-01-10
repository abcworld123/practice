import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(2, len(arr)): arr[i] ^= arr[i - 1]

sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(int(input()))]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
cnt = [0] * (1 << 20)
s, e, cur = 0, 0, 0
cnt[0] = 1
zflag = K == 0

for a, b, i in queries:
    a -= 1
    while a < s:
        s -= 1
        x = arr[s]
        cur += cnt[x ^ K]
        cnt[x] += 1
    while e < b:
        e += 1
        x = arr[e]
        cur += cnt[x ^ K]
        cnt[x] += 1
    while s < a:
        x = arr[s]
        cnt[x] -= 1
        cur -= cnt[x ^ K]
        s += 1
    while b < e:
        x = arr[e]
        cnt[x] -= 1
        cur -= cnt[x ^ K]
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())


# 만약 i = j 이면서 Ai ^ Aj가 불가능한 경우(Ai 또는 Aj 단독) 위 코드가 맞음.
# 만약 Ai ^ Aj가 가능한 경우 아래의 코드가 맞음.
# 현재 BOJ에서는 전자만 가능하다고 채점하고 있음

import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
_arr = arr[:]
for i in range(2, len(arr)): arr[i] ^= arr[i - 1]

sqrtN = 600
queries = [(*map(int, input().split()), i) for i in range(int(input()))]
queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
ans = [0] * len(queries)
cnt = [0] * (1 << 20)
s, e, cur = 0, 0, 0
cnt[0] = 1
kz = K == 0

for a, b, i in queries:
    a -= 1
    while a < s:
        s -= 1
        x = arr[s]
        cnt[x] += 1
        cur += cnt[x ^ K]
        cur -= 1 if kz and _arr[s] == 0 else 0
    while e < b:
        e += 1
        x = arr[e]
        cnt[x] += 1
        cur += cnt[x ^ K]
        cur -= 1 if kz and _arr[e] == 0 else 0
    while s < a:
        x = arr[s]
        cur -= cnt[x ^ K]
        cnt[x] -= 1
        cur += 1 if kz and _arr[s] == 0 else 0
        s += 1
    while b < e:
        x = arr[e]
        cur -= cnt[x ^ K]
        cnt[x] -= 1
        cur += 1 if kz and _arr[e] == 0 else 0
        e -= 1
    ans[i] = cur

os.write(1, '\n'.join(map(str, ans)).encode())
