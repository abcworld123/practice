
import sys
input = sys.stdin.readline

def init(seg, s, e, i):
	if s == e: seg[i] = arr[s]
	else:
		mid = (s + e) >> 1
		seg[i] = init(seg, s, mid, i << 1) ^ init(seg, mid + 1, e, (i << 1) + 1)
	return seg[i]


def xor(seg, lazy, s, e, l, r, i):
	propagation(seg, lazy, s, e, i)
	if r < s or l > e: return 0
	if l <= s and e <= r: return seg[i]
	mid = (s + e) >> 1
	return xor(seg, lazy, s, mid, l, r, i << 1) ^ xor(seg, lazy, mid + 1, e, l, r, (i << 1) + 1)


def update(seg, lazy, s, e, l, r, i, v):
	propagation(seg, lazy, s, e, i)
	if e < l or r < s: return
	elif l <= s and e <= r:
		if (e - s + 1) & 1: seg[i] ^= v
		if s != e:
			lazy[i << 1] ^= v
			lazy[(i << 1) + 1] ^= v
	else:
		mid = (s + e) >> 1
		update(seg, lazy, s, mid, l, r, i << 1, v)
		update(seg, lazy, mid + 1, e, l, r, (i << 1) + 1, v)
		seg[i] = seg[i << 1] ^ seg[(i << 1) + 1]


def propagation(seg, lazy, s, e, i):
	if lazy[i]:
		if (e - s + 1) & 1: seg[i] ^= lazy[i]
		if s != e:
			lazy[i << 1] ^= lazy[i]
			lazy[(i << 1) + 1] ^= lazy[i]
		lazy[i] = 0


n = int(input())
arr = [0] + [*map(int, input().split())]
seg = [0] * (1 << (n.bit_length() + 1))
lazy = seg[:]
init(seg, 1, n, 1)

m = int(input())
for i in range(m):
	x = [*map(int, input().split())]
	if x[0] == 1: update(seg, lazy, 1, n, x[1] + 1, x[2] + 1, 1, x[3])
	else: print(xor(seg, lazy, 1, n, x[1] + 1, x[2] + 1, 1))
