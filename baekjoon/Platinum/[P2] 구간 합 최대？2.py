import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def init(seg, leaf, arr, s, e, i):
    if s == e:
        seg[i] = (arr[s],) * 4
        leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        L = init(seg, leaf, arr, s, m, ch)
        R = init(seg, leaf, arr, m + 1, e, ch + 1)
        build(seg[i], L, R)
    return seg[i]

def get(seg, s, e, l, r, i):
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    L = get(seg, s, m, l, r, ch) if l <= m else (-100000000,) * 4
    R = get(seg, m + 1, e, l, r, ch + 1) if m + 1 <= r else (-100000000,) * 4
    return build([0, 0, 0, 0], L, R)

def update(seg, i, v):
    seg[i] = (v,) * 4
    i >>= 1
    while i:
        seg[i] = build(seg[i], seg[i << 1], seg[(i << 1) + 1])
        i >>= 1

def build(node, L, R):
    node[0] = L[0] if L[0] > L[3] + R[0] else L[3] + R[0]
    node[1] = R[1] if R[1] > R[3] + L[1] else R[3] + L[1]
    node[2] = max(L[2], R[2], L[1] + R[0])
    node[3] = L[3] + R[3]
    return node


def main():
    N, Q, U, V = map(int, input().split())
    arr = [0] + [U * int(x) + V for x in map(int, input().split())]
    seg = [[0, 0, 0, 0] for _ in range(1 << ((N - 1).bit_length() + 1))]
    leaf = [0] * (N + 1)
    ans = __pypy__.builders.StringBuilder()
    init(seg, leaf, arr, 1, N, 1)
    for _ in range(Q):
        C, A, B = map(int, input().split())
        if C == 0:
            ans.append(str(get(seg, 1, N, A, B, 1)[2] - V))
            ans.append('\n')
        else:
            update(seg, leaf[A], U * B + V)

    os.write(1, ans.build().encode())


if __name__ == '__main__': main()
