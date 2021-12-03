import sys
input = sys.stdin.readline

def update(seg, s, e, l, r, i, v):
    ch = i << 1
    if l <= s and e <= r:
        seg[i][0] += (e - s + 1) * v
    else:
        m = (s + e) >> 1
        if l <= m: update(seg, s, m, l, r, ch, v)
        if m + 1 <= r: update(seg, m + 1, e, l, r, ch + 1, v)

    if seg[i][0]: seg[i][1] = e - s + 1
    elif s == e: seg[i][1] = 0
    else: seg[i][1] = seg[ch][1] + seg[ch + 1][1]


def start(lines):
    ans = 0
    seg = [[0, 0] for _ in range(1 << (n.bit_length() + 1))]

    for x, y1, y2, flag in lines:
        prev_area = seg[1][1]
        update(seg, 1, n, y1, y2 - 1, 1, flag)
        ans += abs(seg[1][1] - prev_area)
    return ans


ans = 0
n, halfn = 20002, 10001
lines_x, lines_y = [], []
arr = [list(map(int, input().split())) for _ in range(int(input()))]

for line in arr:
    x1, y1, x2, y2 = line
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    lines_x.append((x1, y1 + halfn, y2 + halfn, 1))
    lines_x.append((x2, y1 + halfn, y2 + halfn, -1))
    lines_y.append((y1, x1 + halfn, x2 + halfn, 1))
    lines_y.append((y2, x1 + halfn, x2 + halfn, -1))
lines_x.sort(key=lambda x: (x[0], -x[3]))
lines_y.sort(key=lambda x: (x[0], -x[3]))

ans += start(lines_x)
ans += start(lines_y)
print(ans)
