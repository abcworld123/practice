import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
ori = [l[:] for l in arr]
visited = [[0] * M for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = []

for i in range(1, N - 1):
	for j in range(1, M - 1):
		if arr[i][j] == 'W':
			q.append((i, j))

for i, j in q:
	for dy, dx in dir:
		y, x = i + dy, j + dx
		if arr[y][x] == '+':
			while arr[y][x] == '+':
				y += dy
				x += dx
			if arr[y][x] == '#':
				y -= dy
				x -= dx
				if not visited[y][x]:
					visited[y][x] = 1
					q.append((y, x))
			elif arr[y][x] == '.' and not visited[y][x]:
				visited[y][x] = 1
				q.append((y, x))
		elif arr[y][x] == '.' and not visited[y][x]:
			visited[y][x] = 1
			q.append((y, x))

for i in range(N):
	for j in range(M):
		if not visited[i][j] and ori[i][j] == '.':
			ori[i][j] = 'P'

print('\n'.join(''.join(l) for l in ori))
