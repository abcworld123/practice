import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def f(arr, ans, x, y, size):
    if size == 3: ch = [arr[y + j][x + i] for i in range(3) for j in range(3)]
    else: ch = [f(arr, ans, x + i * size // 3, y + j * size // 3, size // 3) for i in range(3) for j in range(3)]
    same = all(c == ch[0] for c in ch)
    if same: return ch[0]
    for c in ch:
        if c != 2: ans[c] += 1
    return 2

N = int(input())
t = [-1, 0, 1]
ans = [0, 0, 0]
arr = [list(map(int, input().split())) for _ in range(N)]
s = f(arr, ans, 0, 0, N)
if s != 2: ans[s] += 1

print(ans[-1])
print(ans[0])
print(ans[1])
