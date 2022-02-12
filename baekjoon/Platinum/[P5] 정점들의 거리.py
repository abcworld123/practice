import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
par = [0] * (N + 1)
lvs = [0] * (N + 1)
cost = [0] * (N + 1)
ans = []
q = [(1, 1)]
lvs[1] = 1

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for u, lv in q:
    for v, c in arr[u]:
        if not lvs[v]:
            par[v] = u
            lvs[v] = lv + 1
            cost[v] = c
            q.append((v, lv + 1))

for _ in range(int(input())):
    a, b = map(int, input().split())
    lv_a, lv_b, c = lvs[a], lvs[b], 0
    while lv_a > lv_b:
        c += cost[a]
        a = par[a]
        lv_a -= 1
    while lv_a < lv_b:
        c += cost[b]
        b = par[b]
        lv_b -= 1
    while a != b:
        c += cost[a] + cost[b]
        a = par[a]
        b = par[b]
    ans.append(c)

print('\n'.join(map(str, ans)))


# TLE 받아야 하는데 왜 통과?
