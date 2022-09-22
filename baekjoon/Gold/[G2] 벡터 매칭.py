import sys
input = sys.stdin.readline

def comb(cnt, l):
    if cnt == k:
        sx = total[0] - 2 * cur[0]
        sy = total[1] - 2 * cur[1]
        dist[0] = min(dist[0], sx * sx + sy * sy)
        return
    for i in range(l, N):
        cur[0] += arr[i][0]
        cur[1] += arr[i][1]
        comb(cnt + 1, i + 1)
        cur[0] -= arr[i][0]
        cur[1] -= arr[i][1]

ans = []

for T in range(int(input())):
    N = int(input())
    k = N >> 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = [sum(x[0] for x in arr), sum(x[1] for x in arr)]
    cur = [arr[0][0], arr[0][1]]
    dist = [float('inf')]
    comb(1, 1)
    ans.append(dist[0])

print('\n'.join(map(lambda x: str(x ** .5), ans)))
