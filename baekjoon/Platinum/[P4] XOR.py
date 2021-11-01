import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
	if start == end: segtree[i] = arr[start]
	else:
		mid, child = (start + end) >> 1, i << 1
		segtree[i] = init(segtree, start, mid, child) + init(segtree, mid + 1, end, child + 1)
	return segtree[i]


def summ(segtree, lazy, start, end, left, right, i):
	propagation(segtree, lazy, start, end, i)
	if right < start or left > end: return 0
	if left <= start and end <= right: return segtree[i]
	mid, child = (start + end) >> 1, i << 1
	return summ(segtree, lazy, start, mid, left, right, child) + summ(segtree, lazy, mid + 1, end, left, right, child + 1)


def update(segtree, lazy, start, end, left, right, i, diff):
	propagation(segtree, lazy, start, end, i)
	if end < left or right < start: return
	if start == end: segtree[i] ^= diff
	elif left <= start and end <= right:
		child = i << 1
		segtree[i] ^= diff
		lazy[child] ^= diff
		lazy[child + 1] ^= diff
	else:
		mid, child = (start + end) >> 1, i << 1
		update(segtree, lazy, start, mid, left, right, child, diff)
		update(segtree, lazy, mid + 1, end, left, right, child + 1, diff)
		segtree[i] = segtree[child] + segtree[child + 1]


def propagation(segtree, lazy, start, end, i):
	if lazy[i]:
		child = i << 1
		segtree[i] ^= lazy[i]
		if start != end:
			lazy[child] ^= lazy[i]
			lazy[child + 1] ^= lazy[i]
		lazy[i] = 0


n = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (n.bit_length() + 1))
lazy = segtree[:]
init(segtree, 1, n, 1)

m = int(input())
for i in range(m):
	line = list(map(int, input().split()))
	if line[0] == 1: update(segtree, lazy, 1, n, line[1] + 1, line[2] + 1, 1, line[3])
	else: print(summ(segtree, lazy, 1, n, line[1] + 1, line[1] + 1, 1))
