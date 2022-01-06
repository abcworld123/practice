def f(x1, y1, x2, y2, q):
    if q == 1:
        arr[y1][x1 + 2] = '*'
        arr[y1 + 1][x1 + 1: x1 + 4] = '* *'
        arr[y1 + 2][x1: x1 + 5] = '*****'
        return
    xm, ym = (x1 + x2) >> 1, (y1 + y2) >> 1
    f(x1 + q, y1, xm + q, ym, q >> 1)
    f(x1, ym, xm, y2, q >> 1)
    f(xm, ym, x2, y2, q >> 1)

N = int(input())
arr = [[' '] * (N << 1) for _ in range(N)]
f(0, 0, N << 1, N, N >> 1)

print('\n'.join(''.join(x[:-1]) for x in arr))
