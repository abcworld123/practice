sudoku = [list(map(int, input().split())) for _ in range(9)]
hor, ver, can = [0] * 9, [0] * 9, [0] * 9
can_num = [[0] * 9 for _ in range(9)]
blanks = 0

stack = []
pop_flag = True
h, v, prev = -1, -1, 0

for i in range(9):
	for j in range(9):
		hor[i] ^= 1 << sudoku[i][j]
		ver[i] ^= 1 << sudoku[j][i]
		can_num[i][j] = i // 3 * 3 + j // 3
		can[can_num[i][j]] ^= 1 << sudoku[i][j]
		if sudoku[i][j] == 0:
			blanks += 1
			if h == -1: h, v = i, j
stack.append((h, v, 0))

while stack and len(stack) != blanks:
	if pop_flag:
		h, v, prev = stack.pop()
		n = sudoku[h][v]
		if n:
			b = 1 << n
			sudoku[h][v] = 0
			hor[h] ^= b
			ver[v] ^= b
			can[can_num[h][v]] ^= b
		pop_flag = False
	elif sudoku[h][v]:
		v = (v + 1) % 9
		if v == 0: h += 1
		continue

	for n in range(prev + 1, 10):
		b = 1 << n
		if not hor[h] & b and not ver[v] & b and not can[can_num[h][v]] & b:  # 안 겹침
			sudoku[h][v] = n
			hor[h] ^= b
			ver[v] ^= b
			can[can_num[h][v]] ^= b
			stack.append((h, v, n))
			v = (v + 1) % 9
			if v == 0: h += 1
			prev = 0
			break
	else: pop_flag = True

if stack:
	for i in range(9):
		print(' '.join(map(str, sudoku[i])))
else: print(-1)
