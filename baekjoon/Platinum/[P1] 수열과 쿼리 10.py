import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, arr, s, e, i):
    if s == e: seg[i] = (arr[s],) * 4
    else:
        m, ch = (s + e) >> 1, i << 1
        build(seg[i], init(seg, arr, s, m, ch), init(seg, arr, m + 1, e, ch + 1))
    return seg[i]

def get(seg, s, e, l, r, i):
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    if r < m + 1: return get(seg, s, m, l, r, ch)
    if m < l: return get(seg, m + 1, e, l, r, ch + 1)
    return build([0, 0, 0, 0], get(seg, s, m, l, r, ch), get(seg, m + 1, e, l, r, ch + 1))

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
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2 and y1 == y2:
            ret = get(seg, 1, N, x1, y1, 1)[2]
        elif x1 == x2:
            a = get(seg, 1, N, x1, y1, 1)
            b = get(seg, 1, N, y1 + 1, y2, 1)
            ret = a[1] + b[0] if a[1] + b[0] > a[2] else a[2]
        elif y1 == y2:
            a = get(seg, 1, N, x1, x2 - 1, 1)
            b = get(seg, 1, N, x2, y2, 1)
            ret = a[1] + b[0] if a[1] + b[0] > b[2] else b[2]
        elif x2 - y1 >= 1:
            a = get(seg, 1, N, x1, y1, 1)[1]
            b = get(seg, 1, N, x2, y2, 1)[0]
            c = get(seg, 1, N, y1 + 1, x2 - 1, 1)[3] if x2 - y1 > 1 else 0
            ret = a + b + c
        else:
            a = get(seg, 1, N, x1, x2 - 1, 1)
            b = get(seg, 1, N, x2, y1, 1)
            c = get(seg, 1, N, y1 + 1, y2, 1)
            d = get(seg, 1, N, x2, y2, 1)
            ret = max(a[1] + d[0], b[1] + c[0], b[2])
        ans.append(str(ret))
        ans.append('\n')

    os.write(1, ans.build().encode())


if __name__ == '__main__': main()
