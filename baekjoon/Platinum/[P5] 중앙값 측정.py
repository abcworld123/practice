import sys
input = sys.stdin.readline

def get(seg, s, e, i, x):
    while s != e:
        if x <= seg[i << 1]: e = (s + e) >> 1; i = i << 1
        else: s = ((s + e) >> 1) + 1; x -= seg[i << 1]; i = (i << 1) + 1
    return s

def update(seg, s, e, i, target, diff):
    while s != e:
        seg[i] += diff
        if target <= (s + e) >> 1: e = (s + e) >> 1; i = i << 1
        else: s = ((s + e) >> 1) + 1; i = (i << 1) + 1
    seg[i] += diff
    return s

temp = 65536
N, K = map(int, input().split())
arr = [int(input()) + 1 for _ in range(N)]
seg = [0] * 131072
ans, left, median = 0, K - 1, (K + 1) >> 1

for i in range(K - 1):
    update(seg, 1, temp, 1, arr[i], 1)

for i in range(K - 1, N):
    update(seg, 1, temp, 1, arr[i], 1)
    ans += get(seg, 1, temp, 1, median) - 1
    update(seg, 1, temp, 1, arr[i - left], -1)

print(ans)
