import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, area, s, e, i):
    if s == e: seg[i] = [area[s], 0]
    else:
        seg[i] = [0, 0]
        m, ch = (s + e) >> 1, i << 1
        seg[i][0] = init(seg, area, s, m, ch) + init(seg, area, m + 1, e, ch + 1)
    return seg[i][0]

def summ(seg, lazy, s, e, l, r, i):
    if lazy[i]: propagation(seg, lazy, s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i][1]
    m, ch = (s + e) >> 1, i << 1
    return summ(seg, lazy, s, m, l, r, ch) + summ(seg, lazy, m + 1, e, l, r, ch + 1)

def update(seg, lazy, s, e, l, r, i, v):
    if lazy[i]: propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    if s == e: seg[i][1] += v * seg[i][0]
    elif l <= s and e <= r:
        ch = i << 1
        seg[i][1] += v * seg[i][0]
        lazy[ch] += v
        lazy[ch + 1] += v
    else:
        m, ch = (s + e) >> 1, i << 1
        update(seg, lazy, s, m, l, r, ch, v)
        update(seg, lazy, m + 1, e, l, r, ch + 1, v)
        seg[i][1] = seg[ch][1] + seg[ch + 1][1]

def propagation(seg, lazy, s, e, i):
    ch = i << 1
    seg[i][1] += lazy[i] * seg[i][0]
    if s != e:
        lazy[ch] += lazy[i]
        lazy[ch + 1] += lazy[i]
    lazy[i] = 0


def main():
    N = int(input())
    addq, sumq = [], []
    pos = set()

    for i in range(N):
        q = list(map(int, input().split()))
        if q[0] == 1: addq.append((q[1], q[2] + 1, q[3]))
        else: sumq.append((i, q[1], q[2] + 1, q[3]))
        pos.add(q[1])
        pos.add(q[2] + 1)

    N = len(pos) - 1
    pos = sorted(pos)
    sumq.sort(key=lambda x: x[3])
    comp = {v: i for i, v in enumerate(pos, start=1)}
    area = [0] + [pos[i] - pos[i - 1] for i in range(1, len(pos))]
    sb = __pypy__.builders.StringBuilder()

    seg = [0] * (1 << ((N - 1).bit_length() + 1))
    lazy = seg[:]
    init(seg, area, 1, N, 1)
    ans = []
    j = 0

    for i, q in enumerate(addq, start=1):
        update(seg, lazy, 1, N, comp[q[0]], comp[q[1]] - 1, 1, q[2])
        while j < len(sumq) and sumq[j][3] == i:
            ans.append((sumq[j][0], summ(seg, lazy, 1, N, comp[sumq[j][1]], comp[sumq[j][2]] - 1, 1)))
            j += 1

    for _, x in sorted(ans, key=lambda x: x[0]): sb.append(str(x)); sb.append('\n')
    os.write(1, sb.build().encode())


if __name__ == '__main__': main()
