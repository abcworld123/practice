import sys
input = sys.stdin.readline

def dfs(cur, lv, i):
    if lc[cur] != -1: i = dfs(lc[cur], lv + 1, i)
    i += 1
    w = i - wid[lv] + 1
    if wid[lv] == 0: wid[lv] = i
    elif w == ans[1]: ans[0] = min(ans[0], lv)
    elif w > ans[1]: ans[0] = lv; ans[1] = w
    if rc[cur] != -1: i = dfs(rc[cur], lv + 1, i)
    return i


N = int(input())
lc = [-1] * (N + 1)
rc = [-1] * (N + 1)
wid = [0] * (N + 1)
ch = [0] * (N + 2)
ans = [1, 1]
root = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    ch[b] += 1
    ch[c] += 1
    lc[a] = b
    rc[a] = c
print(ch)
for i in range(1, N + 1):
    if ch[i] == 0: root = i; break

dfs(root, 1, 0)
print(*ans)
