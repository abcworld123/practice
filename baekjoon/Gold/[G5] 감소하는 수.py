def check(n, jari):

	arr = [[]]
	total = 0 if jari else -1
	for i in range(10):
		arr[-1].append(1)
		if len(arr) >= jari: total += 1
		if total >= n: return arr, total

	for j in range(1, 10):
		arr.append([0] * j)
		for i in range(j, 10):
			cur = arr[-2][i - 1] + arr[-1][i - 1]
			arr[-1].append(cur)
			if len(arr) >= jari: total += cur
			if total >= n: return arr, total


n, jari = int(input()), 0
if n >= 1023: print(-1); exit(0)
while 1:
	arr, total = check(n, jari)
	print(len(arr[-1]) - 1, end='')
	n, jari = n - total + arr[-1][-1], len(arr) - 1
	if jari < 1: break
