import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], -x[0]))
ans, t, cur, fl = float('inf'), 0, 0, 0
for w, c in arr:
    if fl != c: fl = c; cur = 0
    t += w
    cur += c
    if t >= M: ans = min(ans, cur)

print(ans if ans != float('inf') else -1)
