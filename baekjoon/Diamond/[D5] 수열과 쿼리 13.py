import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
mod = 10 ** 9 + 7

def init(seg, arr, s, e, i):
    if s == e: seg[i] = arr[s]
    else:
        m, ch = (s + e) >> 1, i << 1
        seg[i] = (init(seg, arr, s, m, ch) + init(seg, arr, m + 1, e, ch + 1)) % mod
    return seg[i]

def summ(seg, lazy, s, e, l, r, i):
    propagation(seg, lazy, s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    return summ(seg, lazy, s, m, l, r, ch) + summ(seg, lazy, m + 1, e, l, r, ch + 1)

def update(seg, lazy, s, e, l, r, i, v, op):
    propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    if s == e:
        if op == 1: seg[i] = (seg[i] + v) % mod
        elif op == 2: seg[i] = (seg[i] * v) % mod
        else: seg[i] = v
    elif l <= s and e <= r:
        if op == 1:
            lazy[i][1] = (lazy[i][1] + v) % mod
        elif op == 2:
            lazy[i][0] = (lazy[i][0] * v) % mod
            lazy[i][1] = (lazy[i][1] * v) % mod
        else:
            lazy[i][0] = 0
            lazy[i][1] = v
        propagation(seg, lazy, s, e, i)

    else:
        m, ch = (s + e) >> 1, i << 1
        update(seg, lazy, s, m, l, r, ch, v, op)
        update(seg, lazy, m + 1, e, l, r, ch + 1, v, op)
        seg[i] = seg[ch] + seg[ch + 1]

def propagation(seg, lazy, s, e, i):
    a, b = lazy[i]
    seg[i] = (a * seg[i] + b * (e - s + 1)) % mod
    if s != e:
        ch = i << 1
        lazy[ch][0] = (lazy[ch][0] * a) % mod
        lazy[ch][1] = (lazy[ch][1] * a) % mod
        lazy[ch][1] = (lazy[ch][1] + b) % mod
        lazy[ch + 1][0] = (lazy[ch + 1][0] * a) % mod
        lazy[ch + 1][1] = (lazy[ch + 1][1] * a) % mod
        lazy[ch + 1][1] = (lazy[ch + 1][1] + b) % mod
    lazy[i][0] = 1
    lazy[i][1] = 0


def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    seg = [0] * (1 << ((N - 1).bit_length() + 1))
    lazy = [[1, 0] for _ in range(1 << ((N - 1).bit_length() + 1))]
    ans = __pypy__.builders.StringBuilder()
    init(seg, arr, 1, N, 1)
    for _ in range(int(input())):
        op, x, y, *v = map(int, input().split())
        if op <= 3:
            update(seg, lazy, 1, N, x, y, 1, v[0], op)
        else:
            ans.append(str(summ(seg, lazy, 1, N, x, y, 1) % mod))
            ans.append('\n')

    os.write(1, ans.build().encode())


if __name__ == '__main__': main()

# 나중에 꼭 성능 개선해보기
