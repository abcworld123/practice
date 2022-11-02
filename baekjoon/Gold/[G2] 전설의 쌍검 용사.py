import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = []
have = [0] * 1000001
s = set()
ans = 0

for i in range(n):
    A, B, C = map(int, input().split())
    arr.append((A, 1, i))
    arr.append((B, 0, i))
    arr.append((C, 2, i))
arr.sort(key=lambda x: (x[0], x[1]))

for x, t, i in arr:
    if t == 0:
        s.add(i)
    elif t == 1:
        if not have[x]:
            have[x] = 1
            ans += 1
            s = {i} if i in s else set()
    else:
        if i in s:
            s.clear()
            ans += 1

print(ans)
