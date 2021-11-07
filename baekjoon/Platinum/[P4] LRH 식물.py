import sys
input = sys.stdin.readline


def get(segtree, lazy, start, end, target, i):
	propagation(segtree, lazy, start, end, i)
	mid, child = (start + end) >> 1, i << 1
	if start == end: flower = segtree[i]
	elif target <= mid: flower = get(segtree, lazy, start, mid, target, child)
	else: flower = get(segtree, lazy, mid + 1, end, target, child + 1)
	segtree[i] -= flower
	return flower


def update(segtree, lazy, start, end, left, right, i, diff):
	propagation(segtree, lazy, start, end, i)
	if end < left or right < start: return
	if start == end: segtree[i] += diff
	elif left <= start and end <= right:
		child = i << 1
		segtree[i] += (end - start + 1) * diff
		lazy[child] += diff
		lazy[child + 1] += diff
	else:
		mid, child = (start + end) >> 1, i << 1
		update(segtree, lazy, start, mid, left, right, child, diff)
		update(segtree, lazy, mid + 1, end, left, right, child + 1, diff)
		segtree[i] = segtree[child] + segtree[child + 1]


def propagation(segtree, lazy, start, end, i):
	if lazy[i]:
		child = i << 1
		segtree[i] += (end - start + 1) * lazy[i]
		if start != end:
			lazy[child] += lazy[i]
			lazy[child + 1] += lazy[i]
		lazy[i] = 0


xmax = 100000
segtree = [0] * (1 << (xmax.bit_length() + 1))
lazy = segtree[:]

for i in range(int(input())):
	L, R = map(int, input().split())
	print(get(segtree, lazy, 1, xmax, L, 1) + get(segtree, lazy, 1, xmax, R, 1))
	if R - L > 1: update(segtree, lazy, 1, xmax, L + 1, R - 1, 1, 1)
