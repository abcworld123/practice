def check(i, j, k):
    a, b, c = 1, 3, 2
    while b <= k:
        if a < i % b <= c and a < j % b <= c: print(' ', end=''); return
        a *= 3; b *= 3; c *= 3
    print('*', end='')

n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        check(i, j, n)
    print()
