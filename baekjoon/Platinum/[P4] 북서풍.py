import sys
input = sys.stdin.readline


def summ(fwtree, i):
	total = 0
	while i:
		total += fwtree[i]
		i -= i & -i
	return total


def update(fwtree, arr, N, i, diff):
	arr[i] += diff
	while i <= N:
		fwtree[i] += diff
		i += i & -i


for case in range(int(input())):
	ps = [list(map(int, input().split())) for _ in range(int(input()))]
	ps.sort(key=lambda x: -x[1])

	rank = 1
	cur_y = ps[0][1]
	for p in ps:
		if p[1] != cur_y:
			rank += 1
			cur_y = p[1]
		p[1] = rank

	arr = [0] * (rank + 1)
	fwtree = arr[:]
	ps.sort(key=lambda x: x[0])
	ans = []

	for x, y in ps:
		ans.append(summ(fwtree, y))
		update(fwtree, arr, rank, y, 1)
	print(sum(ans))
