from collections import deque

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
queue = deque([(0, 0, 1 << (ord(arr[0][0]) - 65), 1)])
history = [[set() for _ in range(C)] for _ in range(R)]
ans = 1

while queue:
	y, x, visited, cnt = queue.popleft()
	_dir = ((y > 0, y - 1, x), (y < R - 1, y + 1, x), (x > 0, y, x - 1), (x < C - 1, y, x + 1))
	cnt += 1
	for cond, _y, _x in _dir:
		if not cond: continue
		c = 1 << (ord(arr[_y][_x]) - 65)
		if not visited & c and visited not in history[_y][_x]:
			history[_y][_x].add(visited)
			if ans < cnt: ans = cnt
			queue.append((_y, _x, visited ^ c, cnt))

print(ans)
