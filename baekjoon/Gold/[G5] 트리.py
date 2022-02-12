def dfs(cur, leaf):
    if not chs[cur]: return leaf + 1
    for ch in chs[cur]: leaf = dfs(ch, leaf)
    return leaf

N = int(input())
chs = [[] for _ in range(N + 1)]
arr = map(int, input().split())
rm = int(input())
root = 0

for i, x in enumerate(arr):
    if x == -1: root = i
    elif i != rm: chs[x].append(i)

print(dfs(root, 0) if root != rm else 0)
