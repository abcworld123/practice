import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def get(seg, lazy, s, e, l, r, i):
	if lazy[i]: propagation(seg, lazy, s, e, i)
	if r < s or l > e: return 0
	if l <= s and e <= r: return seg[i]
	m, ch = (s + e) >> 1, i << 1
	return max(get(seg, lazy, s, m, l, r, ch), get(seg, lazy, m + 1, e, l, r, ch + 1))

def update(seg, lazy, s, e, l, r, i, v):
	if lazy[i]: propagation(seg, lazy, s, e, i)
	if e < l or r < s: return
	elif l <= s and e <= r:
		lazy[i] = v
		propagation(seg, lazy, s, e, i)
	else:
		m, ch = (s + e) >> 1, i << 1
		update(seg, lazy, s, m, l, r, ch, v)
		update(seg, lazy, m + 1, e, l, r, ch + 1, v)
		seg[i] = max(seg[ch], seg[ch + 1])

def propagation(seg, lazy, s, e, i):
	seg[i] = lazy[i]
	if s != e:
		ch = i << 1
		lazy[ch] = lazy[i]
		lazy[ch + 1] = lazy[i]
	lazy[i] = 0


N = int(input())
arr = []
comp = set()

for _ in range(N):
	r, l = map(int, input().split())
	r += l
	comp.add(l)
	comp.add(r)
	arr.append([l, r])

comp = {x: i for i, x in enumerate(sorted(comp), start=1)}
n = len(comp)
seg = [0] * (1 << ((n - 1).bit_length() + 1))
lazy = seg[:]

for l, r in arr:
	l, r = comp[l], comp[r] - 1
	high = get(seg, lazy, 1, n, l, r, 1)
	update(seg, lazy, 1, n, l, r, 1, high + 1)

print(seg[1])
