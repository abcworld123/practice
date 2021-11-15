import sys
input = sys.stdin.readline

while 1:
    N = int(input())
    if N == 0: break
    arr = input().split()
    pair = input().split()
    pair = {pair[N - i]: i for i in range(1, N + 1)}
    fw = [0] * (N + 2)
    ans = 0

    for x in arr:
        i, j = pair[x] - 1, pair[x]
        while i: ans += fw[i]; i -= i & -i
        while j <= N: fw[j] += 1; j += j & -j

    print(ans)
