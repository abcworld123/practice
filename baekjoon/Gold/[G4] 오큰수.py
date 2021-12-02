import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
t = tuple(map(int, input().split()))
s, top = [0] * (len(t) + 1), 0
s[0] = 9999999
ans = [0] * len(t)

for i in range(len(t) - 1, -1, -1):
    while s[top] <= t[i]: top -= 1
    ans[i] = s[top] if top else -1
    top += 1
    s[top] = t[i]

sys.stdout.write(' '.join(map(str, ans)))
