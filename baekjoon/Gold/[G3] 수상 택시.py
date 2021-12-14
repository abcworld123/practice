import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        arr.append((a, 1))
        arr.append((b, -1))
arr.sort(key=lambda x: x[0])

ans, cur, turn, back = 0, 0, 0, 0
for a, b in arr:
    ans += a - cur
    cur = a
    if b < 0:
        if back == 0: turn = a
        back += 1
    else:
        back -= 1
        if back == 0: ans += 2 * (cur - turn)
ans += M - cur

print(ans)
