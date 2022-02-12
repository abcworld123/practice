import sys
input = sys.stdin.readline
sys.setrecursionlimit(11000)

def dfs(cur, l):
    if not arr[cur]: return l
    l1, l2 = l, l
    for ch, cost in arr[cur]:
        cl = dfs(ch, l + cost)
        if cl > l1: l1, l2 = cl, l1
        elif cl > l2: l2 = cl
    dia = l1 + l2 - 2 * l
    ans[0] = max(dia, ans[0])
    return l1


N = int(input())
arr = [[] for _ in range(N + 1)]
ans = [0]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

dfs(1, 0)
print(ans[0])
