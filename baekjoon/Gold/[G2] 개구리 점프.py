import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, Q = map(int, input().split())
groups = [0] * (N + 1)
arr, ans = [], []

for i in range(1, N + 1):
    l, r, _ = input().split()
    arr.append((int(l), int(r), i))
arr.sort(key=lambda x: x[0])

cur = 0
s, e = -1, -1
for l, r, g in arr:
    if e < l:
        cur += 1
        s = l
        e = r
    else:
        e = max(e, r)
    groups[g] = cur

for _ in range(Q):
    a, b = input().split()
    ans.append(1 if groups[int(a)] == groups[int(b)] else 0)

os.write(1, '\n'.join(map(str, ans)).encode())
