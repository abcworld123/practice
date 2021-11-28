import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
l, ans = [], 1
for _ in range(N):
    x, r = map(int, input().split())
    l.append((x - r, x + r))

l.sort(key=lambda x: (x[0], -x[1]))
l.append((float('inf'), float('inf')))
s = [[l[0], l[0][0]]]

for i in range(1, len(l)):
    c = l[i]
    while s and s[-1][0][1] <= c[0]:
        if s[-1][0][1] == s[-1][1]: ans += 1
        s.pop()
        ans += 1
    if s and c[0] == s[-1][1]:
        s[-1][1] = c[1]
    s.append([c, c[0]])

print(ans)
