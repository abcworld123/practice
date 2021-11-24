import sys
input = sys.stdin.readline


def dfs(s, e, i):
    if s == e: sys.stdout.write(str(seg[i][0]) + '\n')
    else:
        m, ch = (s + e) >> 1, i << 1
        propagation(i, ch)
        propagation(i, ch + 1)
        dfs(s, m, ch)
        dfs(m + 1, e, ch + 1)


def update(s, e, l, r, i, v, op):
    if op == 1 and seg[i][0] >= v: return
    if op == 2 and seg[i][1] <= v: return
    if s == e:
        seg[i][0] = v
        seg[i][1] = v
    else:
        m, ch = (s + e) >> 1, i << 1
        propagation(i, ch)
        propagation(i, ch + 1)
        if l <= s and e <= r:
            if op == 1:
                seg[i][0] = v
                if seg[i][0] > seg[i][1]:
                    seg[i][1] = seg[i][0]
            else:
                seg[i][1] = v
                if seg[i][0] > seg[i][1]:
                    seg[i][0] = seg[i][1]
        else:
            if l <= m: update(s, m, l, r, ch, v, op)
            if m + 1 <= r: update(m + 1, e, l, r, ch + 1, v, op)
            seg[i][0] = min(seg[ch][0], seg[ch + 1][0])
            seg[i][1] = max(seg[ch][1], seg[ch + 1][1])


def propagation(i, ch):
    if seg[ch][0] < seg[i][0]:
        seg[ch][0] = seg[i][0]
        if seg[ch][0] > seg[ch][1]:
            seg[ch][1] = seg[ch][0]
    if seg[ch][1] > seg[i][1]:
        seg[ch][1] = seg[i][1]
        if seg[ch][0] > seg[ch][1]:
            seg[ch][0] = seg[ch][1]


n, k = map(int, input().split())
seg = [[0, 0] for _ in range((1 << (n.bit_length() + 1)))]

for i in range(k):
    op, l, r, v = list(map(int, input().split()))
    update(1, n, l + 1, r + 1, 1, v, op)

dfs(1, n, 1)
