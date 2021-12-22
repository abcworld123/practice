import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

ans, last = 0, -1
for s, e in sorted([(*map(int, input().split()),) for _ in range(int(input()))]):
    if last <= s: ans += 1; last = e
    elif e < last: last = e
print(ans)
