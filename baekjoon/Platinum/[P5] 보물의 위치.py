import sys
input = sys.stdin.readline


def dig(n):
    if n < 10: return n
    return dig(sum(map(int, str(n))))


arr = [None, ((1,), False), ((1, 2, 4, 8, 7, 5), True), ((1, 3, 9), False), ((1, 4, 7), True), ((1, 5, 7, 8, 4, 2), True), ((1, 6, 9), False), ((1, 7, 4), True), ((1, 8), True), ((1, 9), False)]

for i in range(int(input())):
    K, M = map(int, input().split())
    pos = [0, 0]
    _dir = ((1, 1), (0, 1), (1, -1), (0, -1))
    n = dig(M)
    if arr[n][1] == True:
        K %= len(arr[n][0]) * 4
        for j in range(K): pos[_dir[j % 4][0]] += arr[n][0][j % len(arr[n][0])] * _dir[j % 4][1]
        print(*pos)
    else:
        go = min(len(arr[n][0]) - 1, K)
        for j in range(go): pos[_dir[j][0]] += arr[n][0][j] * _dir[j][1]
        for j in range(go, (K - go) % 4 + go): pos[_dir[j % 4][0]] += arr[n][0][-1] * _dir[j % 4][1]
        print(*pos)
