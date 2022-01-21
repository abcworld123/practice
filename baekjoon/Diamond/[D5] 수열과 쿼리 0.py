import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


sqn = 316
N = int(input())
arr = [0] + list(map(int, input().split()))
for i in range(2, N + 1): arr[i] += arr[i - 1]

M = int(input())
q = [(*map(int, input().split()), i) for i in range(M)]
q.sort(key=lambda x: (x[0] // sqn, x[1]))
q.append((N + 1, N + 1, -1))

ans = [0] * M
S, E = [-1] * (2 * N + 1), [-1] * (2 * N + 1)
s, e, i = q[0]
j = 0

for sq in range(sqn + 2):
    m = min((sq + 1) * sqn, N + 1)
    for k in range(sq * sqn, N + 1): S[arr[k]] = E[arr[k]] = -1
    while e < m:
        cur = 0
        for k in range(s - 1, e + 1):
            if S[arr[k]] != -1: cur = max(cur, k - S[arr[k]])
            else: S[arr[k]] = k
        ans[i] = cur
        for k in range(s - 1, e + 1): S[arr[k]] = -1
        j += 1
        s, e, i = q[j]

    cur, l, r = 0, m, m - 1
    while s < m:
        while r < e:
            r += 1
            if S[arr[r]] != -1:
                cur = max(cur, r - S[arr[r]])
                E[arr[r]] = r
            else: E[arr[r]] = S[arr[r]] = r
        t = cur
        while s - 1 < l:
            l -= 1
            if E[arr[l]] != -1: cur = max(cur, E[arr[l]] - l)
            else: E[arr[l]] = l
        ans[i] = cur
        cur = t
        while l < m:
            if E[arr[l]] < m: E[arr[l]] = -1
            l += 1
        j += 1
        s, e, i = q[j]

os.write(1, '\n'.join(map(str, ans)).encode())
