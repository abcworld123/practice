import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
ans[1] = -1

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = [1]
for v in q:
    for ch in tree[v]:
        if not ans[ch]:
            ans[ch] = v
            q.append(ch)

print('\n'.join(map(str, ans[2:])))
