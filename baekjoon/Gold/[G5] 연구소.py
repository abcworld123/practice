maze_ori, b, ans = [], [], 0
N, M = map(int, input().split())
for row in range(N): maze_ori += list(map(int, input().split()))
for i in range(N * M):
	if maze_ori[i] == 0: b.append(i)

for i in range(len(b) - 2):
	for j in range(i + 1, len(b)):
		for k in range(j + 1, len(b)):

			maze = maze_ori[:]
			maze[b[i]], maze[b[j]], maze[b[k]] = 1, 1, 1
			queue = []
			for v in range(N * M):
				if maze[v] == 2: queue.append(v)

			for v in queue:
				if maze[v] == 2:
					U, R, D, L = v - M, v + 1, v + M, v - 1
					if maze[U] == 0 and U >= 0: maze[U] = 2; queue.append(U)
					if R < N * M and maze[R] == 0 and R % M : maze[R] = 2; queue.append(R)
					if D < N * M and maze[D] == 0: maze[D] = 2; queue.append(D)
					if maze[L] == 0 and L % M != M - 1: maze[L] = 2; queue.append(L)

			safe = maze.count(0)
			if ans < safe: ans = safe

print(ans)
