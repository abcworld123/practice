import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
arr = list(map(int, input().split())) + [0, 0]
ans = 0

for i in range(N):
    if arr[i]:
        arr[i + 1] ^= 1
        arr[i + 2] ^= 1
        ans += 1

print(ans)
