N, M = map(int, input().split())
arr = [['.'] * (M + 2)] + [['.'] + list(map(int, input().split())) + ['.'] for _ in range(N)] + [['.'] * (M + 2)]
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans, r = 0, 0
for i in range(1, N + 1): r += arr[i].count(1)

while r:
    q = [(1, 1)]
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    visited[1][1] = 1
    remove = set()
    for i, j in q:
        for dy, dx in d:
            y, x = i + dy, j + dx
            if arr[y][x] == 0:
                if not visited[y][x]:
                    visited[y][x] = 1
                    q.append((y, x))
            elif arr[y][x] == 1:
                visited[y][x] += 1
                if visited[y][x] == 2:
                    remove.add((y, x))
    for i, j in remove:
        arr[i][j] = 0
        r -= 1
    ans += 1

print(ans)
