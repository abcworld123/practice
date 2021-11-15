import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(x + '\n')

def init(seg, s, e, i):
    if s == e: seg[i] = 1
    else:
        seg[i] = init(seg, s, (s + e) >> 1, i << 1) + init(seg, ((s + e) >> 1) + 1, e, (i << 1) + 1)
    return seg[i]


def get(seg, s, e, k, i):
    while s != e:
        seg[i] -= 1
        if k <= seg[i << 1]: e = (s + e) >> 1; i = i << 1
        else: s = ((s + e) >> 1) + 1; k -= seg[i << 1]; i = (i << 1) + 1
    seg[i] -= 1
    return s


N, K = map(int, input().split())
maxN = N
seg = [0] * (1 << (maxN.bit_length() + 1))
init(seg, 1, maxN, 1)
cur, _cur = K, K
K -= 1
ans = []

for i in range(N):
    ans.append(get(seg, 1, maxN, cur, 1))
    N -= 1
    cur = _cur + K
    if 0 < N < cur: cur %= N
    if cur == 0: cur = N
    _cur = cur

print('<' + str(ans)[1: -1] + '>')
