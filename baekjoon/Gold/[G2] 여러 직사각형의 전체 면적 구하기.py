import sys
input = sys.stdin.readline


def update(seg, s, e, l, r, i, d):
	child = i << 1
	if e < l or r < s: return
	if s == e:
		seg[i][0] += d
	elif l <= s and e <= r:
		child = i << 1
		seg[i][0] += (e - s + 1) * d
	else:
		mid = (s + e) >> 1
		update(seg, s, mid, l, r, child, d)
		update(seg, mid + 1, e, l, r, child + 1, d)

	if seg[i][0]: seg[i][1] = e - s + 1
	elif s == e: seg[i][1] = 0
	else: seg[i][1] = seg[child][1] + seg[child + 1][1]


lines = []
n = 30000
area = 0
for _ in range(int(input())):
	x1, y1, x2, y2 = map(lambda x: int(float(x) * 10), input().split())
	x2, y2 = x1 + x2, y1 + y2
	lines.append((x1 + 1, y1 + 1, y2 + 1, 1))
	lines.append((x2 + 1, y1 + 1, y2 + 1, -1))
lines.sort(key=lambda x: x[0])

segtree = [[0, 0] for _ in range((1 << (n.bit_length() + 1)))]
last_x = lines[0][0]

for x, y1, y2, flag in lines:
	dx = x - last_x
	area += dx * segtree[1][1]
	update(segtree, 1, n, y1, y2 - 1, 1, flag)
	last_x = x

print((area / 100) if area % 100 != 0 else int(area / 100))
