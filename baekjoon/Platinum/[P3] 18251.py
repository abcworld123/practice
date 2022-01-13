import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    if max(arr) <= 0: print(max(arr)); return
    arr = iter(arr)
    len_floor = N.bit_length()
    floor = [[(j + N, next(arr)) for j in range((1 << (i - 1)), N + 1, 1 << i)] for i in range(len_floor, 0, -1)][::-1]
    ans = 0

    for i in range(len_floor):
        seg = [[0, 0, 0, 0] for _ in range(2 * (N + 1))]
        while i < len_floor:
            for k, v in floor[i]:
                seg[k] = (seg[k][0] + v,) * 4
                k >>= 1
                while k:
                    cur, L, R = seg[k], seg[k << 1], seg[k << 1 | 1]
                    cur[0] = L[0] if L[0] > L[3] + R[0] else L[3] + R[0]
                    cur[1] = R[1] if R[1] > R[3] + L[1] else R[3] + L[1]
                    cur[2] = max(L[2], R[2], L[1] + R[0])
                    cur[3] = L[3] + R[3]
                    k >>= 1
            ans = max(ans, seg[1][2])
            i += 1
    print(ans)

main()
