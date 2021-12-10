import os, io
from collections import defaultdict
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def init(leaf, s, e, i):
    if s == e: leaf[s] = i
    else:
        init(leaf, s, (s + e) // 2, i * 2)
        init(leaf, (s + e) // 2 + 1, e, i * 2 + 1)


def main():
    blue = [list(map(int, input().split())) for _ in range(int(input()))]
    red = [list(map(int, input().split())) for _ in range(int(input()))]
    comp = {x: c for c, x in enumerate(sorted(set(g[0] for g in blue + red)), start=1)}
    c1, c2 = map(int, input().split())
    n = len(comp)
    seg_size = 1 << ((n - 1).bit_length() + 1)
    leaf = [0] * (n + 1)
    floor = defaultdict(list)
    init(leaf, 1, n, 1)

    for x, y in blue: floor[y].append((leaf[comp[x]], c1))
    for x, y in red: floor[y].append((leaf[comp[x]], -c2))
    floor = [p[1] for p in sorted(floor.items(), key=lambda x: x[0])]
    len_floor = len(floor)
    ans = 0

    for i in range(len_floor):
        if all(g[1] <= 0 for g in floor[i]): continue
        seg = [[0, 0, 0, 0] for _ in range(seg_size)]
        y = i
        while y < len_floor:
            for j, v in floor[y]:
                seg[j] = (seg[j][0] + v,) * 4
                j //= 2
                while j:
                    cur, L, R = seg[j], seg[j * 2], seg[j * 2 + 1]
                    cur[0] = L[0] if L[0] > L[3] + R[0] else L[3] + R[0]
                    cur[1] = R[1] if R[1] > R[3] + L[1] else R[3] + L[1]
                    cur[2] = max(L[2], R[2], L[1] + R[0])
                    cur[3] = L[3] + R[3]
                    j //= 2
            if ans < seg[1][2]: ans = seg[1][2]
            y += 1
    print(ans)


if __name__ == '__main__': main()
