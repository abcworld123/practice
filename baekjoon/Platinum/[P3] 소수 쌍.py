def dfs(visited, R, a):
    visited[a] = True
    for b in graph[a]:
        if R[b] == -1 or (not visited[R[b]] and dfs(visited, R, R[b])):
            R[a] = b
            R[b] = a
            return True
    return False


N = int(input())
arr = list(map(int, input().split()))
prime = set([2] + [x for x in range(3, 2000) if x & 1 and all((x % y for y in range(3, int(x ** .5) + 1, 2)))])
graph = [[] for _ in range(N)]
ans, first = [], []

for i in range(1, N):
    if arr[0] + arr[i] in prime: first.append(i)

for i in range(1, N - 1):
    for j in range(i + 1, N):
        if arr[i] + arr[j] in prime:
            graph[i].append(j)
            graph[j].append(i)

for x in first:
    R = [-1] * N
    R[x] = 0
    pair = 2
    for i in range(1, N):
        if R[i] == -1 and dfs([False] * N, R, i): pair += 2
    if pair == N: ans.append(arr[x])

print(*sorted(ans)) if ans else print(-1)
