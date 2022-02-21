from sys import stdin

def init(leaf, s, e, i):
    if s == e:
        leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        seg[i] = init(leaf, s, m, ch) + init(leaf, m + 1, e, ch + 1)
    return seg[i]

def middle(seg, s, e, i, x):
    while s != e:
        m, ch = (s + e) >> 1, i << 1
        if seg[ch] < x:
            x -= seg[ch]
            s = m + 1
            i = ch + 1
        else:
            e = m
            i = ch
    return s

def update(seg, i):
    while i:
        seg[i] += 1
        i >>= 1


seg = [0] * (1 << ((200000).bit_length() + 1))
leaf = [0] * 20002
init(leaf, 1, 20001, 1)
ans = []

stdin.readline()
for i, x in enumerate(map(int, stdin.read().split()), start=2):
    update(seg, leaf[x + 10001])
    ans.append(middle(seg, 1, 20001, 1, i // 2) - 10001)

print('\n'.join(map(str, ans)))
