import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]
p = {v: k for k, v in enumerate(sorted(set(arr)))}
seg = [0] * (1 << (N.bit_length() + 1))

for x in arr:
    s, e, rank, i, x = 1, N, 1, 1, p[x] + 1
    while s != e:
        seg[i] += 1
        m, ch = (s + e) >> 1, i << 1
        if x <= m: e = m; rank += seg[ch + 1]; i = ch
        else: s = m + 1; i = ch + 1
    seg[i] += 1
    print(rank)
