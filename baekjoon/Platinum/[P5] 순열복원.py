import sys
input = sys.stdin.readline

def init(seg, s, e, i):
    if s == e: seg[i] = 1
    else: seg[i] = init(seg, s, (s + e) >> 1, i << 1) + init(seg, ((s + e) >> 1) + 1, e, (i << 1) + 1)
    return seg[i]

def get(seg, s, e, i, x):
    while s != e:
        seg[i] -= 1
        if x <= seg[i << 1]: e = (s + e) >> 1; i = i << 1
        else: s = ((s + e) >> 1) + 1; x -= seg[i << 1]; i = (i << 1) + 1
    seg[i] -= 1
    return s

N = int(input())
seg = [-1] * (1 << (N.bit_length() + 1))
init(seg, 1, N, 1)
arr = [N - get(seg, 1, N, 1, x + 1) + 1 for x in tuple(map(int, input().split()))[::-1]]
print(*[k[0] + 1 for k in sorted(enumerate(arr[::-1]), key=lambda x: x[1])])
