def f(cur, start_i, end_i, j, m):

	if len(cur) == L:
		if j >= 2 and m >= 1:
			for c in cur: print(c, end='')
			print()
		return

	for i in range(start_i, end_i + 1):
		cur.append(arr[i])
		if arr[i] in moeum: f(cur, i + 1, end_i + 1, j, m + 1)
		else: f(cur, i + 1, end_i + 1, j + 1, m)
		cur.pop()


L, C = map(int, input().split())
arr = [''] + sorted(input().split())
moeum = ['a', 'e', 'i', 'o', 'u']
f([], 1, C - L + 1, 0, 0)
