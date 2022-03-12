import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
tick = [[0] * C for _ in range(R)]
cleaner = [x[0] for x in arr].index(-1)
r1, r2 = cleaner, cleaner + 1
d1 = [(i, 0) for i in range(r1 - 1, -1, -1)] + [(0, j) for j in range(1, C)] + [(i, C - 1) for i in range(1, r1)] + [(r1, j) for j in range(C - 1, -1, -1)]
d2 = [(i, 0) for i in range(r2 + 1, R, 1)] + [(R - 1, j) for j in range(1, C)] + [(i, C - 1) for i in range(R - 2, r2 - 1, -1)] + [(r2, j) for j in range(C - 2, -1, -1)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr[r2][0] = 0
arr[r1][0] = 0

for _ in range(T):
	# step 1
	for i in range(R):
		for j in range(C):
			if arr[i][j]:
				cnt = 0
				unit = int(arr[i][j] / 5)
				for dy, dx in dir:
					y, x = i + dy, j + dx
					if 0 <= y < R and 0 <= x < C and not (x == 0 and (y == r1 or y == r2)):
						tick[y][x] += unit
						cnt += 1
				tick[i][j] -= unit * cnt
	for i in range(R):
		for j in range(C):
			if tick[i][j]:
				arr[i][j] += tick[i][j]
				tick[i][j] = 0
	arr[r1][0] = 0
	arr[r2][0] = 0

	# step 2
	for i in range(1, len(d1)):
		arr[d1[i - 1][0]][d1[i - 1][1]] = arr[d1[i][0]][d1[i][1]]
	for i in range(1, len(d2)):
		arr[d2[i - 1][0]][d2[i - 1][1]] = arr[d2[i][0]][d2[i][1]]

print(sum(sum(line) for line in arr))
