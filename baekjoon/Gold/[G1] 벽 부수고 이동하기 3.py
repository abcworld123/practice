import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [2] * (M + 2) + sum([[2] + list(map(int, input().rstrip())) + [2] for _ in range(N)], []) + [2] * (M + 2)
visited = [[99] * ((M + 2) * (N + 2)) for _ in range(2)]
d = (-M - 2, 1, M + 2, -1, 0)
q = deque([(M + 3, 1, 0, 1)])
end = (M + 2) * (N + 1) - 2

while q:
    i, m, b, t = q.popleft()
    if i == end: print(m); exit()
    for dx in d:
        x = i + dx
        if arr[x] == 0:
            if b < visited[t][x]:
                visited[t][x] = b
                q.append((x, m + 1, b, t ^ 1))
        elif arr[x] == 1 and b < visited[t][x]:
            if dx == 0:
                visited[t][x] = b
                q.append((x, m + 1, b, t ^ 1))
            elif t and b < K:
                visited[t][x] = b
                q.append((x, m + 1, b + 1, t ^ 1))

print(-1)
