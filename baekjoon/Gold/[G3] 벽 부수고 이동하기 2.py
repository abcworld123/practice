import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[2] * (M + 2)] + [[2] + list(map(int, input().rstrip())) + [2] for _ in range(N)] + [[2] * (M + 2)]
visited = [[[False] * (M + 2) for _ in range(N + 2)] for _ in range(K + 1)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = deque([(1, 1, 1, 0)])

while q:
    i, j, m, b = q.popleft()
    if i == N and j == M: print(m); exit()
    for dy, dx in d:
        y, x = i + dy, j + dx
        if arr[y][x] == 0:
            if not visited[b][y][x]:
                visited[b][y][x] = True
                q.append((y, x, m + 1, b))
        elif arr[y][x] == 1 and b < K:
            if not visited[b][y][x]:
                visited[b][y][x] = True
                q.append((y, x, m + 1, b + 1))

print(-1)
