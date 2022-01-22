import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

trie = [None, None, [1, 0]]
cur = trie
ans = []
for i in range(30): cur[0] = [None, None, [1, 0]]; cur = cur[0]

for _ in range(int(input())):
	q, x = map(int, input().split())
	cur, b = trie, 536870912
	if q == 1 or q == 2:
		s = 1 if q == 1 else -1
		while b:
			xb = 1 if x & b else 0
			cur[2][xb] += 1 * s
			if not cur[xb]: cur[xb] = [None, None, [0, 0]]
			cur = cur[xb]
			b >>= 1
	else:
		num = 0
		while b:
			nxb = 0 if x & b else 1
			to = nxb if cur[2][nxb] else (nxb ^ 1)
			num += b * to
			cur = cur[to]
			b >>= 1
		ans.append(num ^ x)

os.write(1, '\n'.join(map(str, ans)).encode())
