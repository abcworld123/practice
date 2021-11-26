import sys
input = sys.stdin.readline

N = int(input())
pair = {}
for i in range(1, N + 1): pair[int(input())] = i

ans = []
fwu = [0] * (N + 1)
fwd = [0] * (N + 1)
x = (N + 2) >> 1
d = -1 if N & 1 else 1

for i in range(N):
    x += d * i
    d *= -1
    s = 0
    ui, di = x - 1, pair[x] - 1
    uj, dj = x, pair[x]
    while ui: s += fwu[ui]; ui -= ui & -ui
    while di: s += fwd[di]; di -= di & -di
    while uj <= N: fwu[uj] += 1; uj += uj & -uj
    while dj <= N: fwd[dj] += 1; dj += dj & -dj
    ans.append(str(i - abs(i - s)))

sys.stdout.write('\n'.join(ans[::-1]))
