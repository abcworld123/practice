import sys
input = sys.stdin.readline


def update(seg, start, end, left, right, i, diff):
	child = i << 1
	if end < left or right < start: return
	if start == end:
		seg[i][0] += diff
	elif left <= start and end <= right:
		child = i << 1
		seg[i][0] += (end - start + 1) * diff
	else:
		mid = (start + end) >> 1
		update(seg, start, mid, left, right, child, diff)
		update(seg, mid + 1, end, left, right, child + 1, diff)

	if seg[i][0]: seg[i][1] = end - start + 1
	elif start == end: seg[i][1] = 0
	else: seg[i][1] = seg[child][1] + seg[child + 1][1]


lines = []
n = 30000
area = 0
for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
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

print(area)
