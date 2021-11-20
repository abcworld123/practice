import sys
input = sys.stdin.readline


def get(seg, s, e, x, i):
    L0, L1, R0, R1 = 0, 0, 0, 0
    while s != e:
        seg[i][0] += 1
        seg[i][1] += x - 1
        m, ch = (s + e) >> 1, i << 1
        if x <= m:
            R0 += seg[ch + 1][0]
            R1 += seg[ch + 1][1]
            e = m
            i = ch
        else:
            L0 += seg[ch][0]
            L1 += seg[ch][1]
            s = m + 1
            i = ch + 1
    seg[i][0] += 1
    seg[i][1] += x - 1
    return L0, L1, R0, R1


N = int(input())
max_x = 200001
seg = [[0, 0] for _ in range(1 << (max_x.bit_length() + 1))]
ans = 1

for i in range(N):
    x = int(input())
    L0, L1, R0, R1 = get(seg, 1, max_x, x + 1, 1)
    if i > 0: ans = (ans * (x * L0 - L1 + R1 - x * R0)) % 1000000007

print(ans)
