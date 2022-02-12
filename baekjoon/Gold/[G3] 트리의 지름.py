import os, io, sys
sys.setrecursionlimit(101000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def dfs(cur, par, l):
    if len(arr[cur]) == 1 and arr[cur][0] == par: return l
    l1, l2 = l, l
    for ch, cost in arr[cur]:
        if ch == par: continue
        cl = dfs(ch, cur, l + cost)
        if cl > l1: l1, l2 = cl, l1
        elif cl > l2: l2 = cl
    dia = l1 + l2 - 2 * l
    ans[0] = max(dia, ans[0])
    return l1


N = int(input())
if N == 0: print(0); exit()
arr = [[] for _ in range(N + 1)]
ans = [0]

for _ in range(N):
    a, *adj, _ = list(map(int, input().split()))
    for i in range(0, len(adj), 2):
        arr[a].append((adj[i], adj[i + 1]))

dfs(1, 0, 0)
print(ans[0])
