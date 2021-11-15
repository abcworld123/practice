import sys
input = sys.stdin.readline

for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(K)]
    arr.sort()
    fw = [0] * (N + 1)
    ans = 0

    for a, b in arr:
        i, j = M - b, M - b + 1
        while i: ans += fw[i]; i -= i & -i
        while j <= N: fw[j] += 1; j += j & -j

    print(f'Test case {case}: {ans}')
