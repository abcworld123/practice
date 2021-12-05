import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def init(seg, arr, s, e, i):
    if s == e:
        seg[i] = (arr[s],) * 4
    else:
        m, ch = (s + e) >> 1, i << 1
        L = init(seg, arr, s, m, ch)
        R = init(seg, arr, m + 1, e, ch + 1)
        build(seg[i], L, R)
    return seg[i]

def get(seg, s, e, l, r, i):
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    L = get(seg, s, m, l, r, ch) if l <= m else (-100000000,) * 4
    R = get(seg, m + 1, e, l, r, ch + 1) if m + 1 <= r else (-100000000,) * 4
    return build([0, 0, 0, 0], L, R)

def build(node, L, R):
    node[0] = L[0] if L[0] > L[3] + R[0] else L[3] + R[0]
    node[1] = R[1] if R[1] > R[3] + L[1] else R[3] + L[1]
    node[2] = max(L[2], R[2], L[1] + R[0])
    node[3] = L[3] + R[3]
    return node


def main():
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    seg = [[0, 0, 0, 0] for _ in range(1 << ((N - 1).bit_length() + 1))]
    ans = __pypy__.builders.StringBuilder()
    init(seg, arr, 1, N, 1)

    for _ in range(int(input())):
        l, r = map(int, input().split())
        ans.append(f'{get(seg, 1, N, l, r, 1)[2]}\n')

    os.write(1, ans.build().encode())


if __name__ == '__main__': main()
