import sys
input = sys.stdin.readline


def update(seg1, seg2, s, e, l, r, i, diff):
    ch = i << 1
    if s == e:
        seg1[i] += diff
    elif l <= s and e <= r:
        seg1[i] += (e - s + 1) * diff
    else:
        m = (s + e) >> 1
        if l <= m: update(seg1, seg2, s, m, l, r, ch, diff)
        if m + 1 <= r: update(seg1, seg2, m + 1, e, l, r, ch + 1, diff)

    if seg1[i]: seg2[i] = e - s + 1
    elif s == e: seg2[i] = 0
    else: seg2[i] = seg2[ch] + seg2[ch + 1]


for case in range(int(input())):
    lines = []
    n, area = 0, 0
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append((x1 + 1, y1 + 1, y2 + 1, 1))
        lines.append((x2 + 1, y1 + 1, y2 + 1, -1))
        if n < x2: n = x2
        if n < y2: n = y2
    lines.sort(key=lambda x: x[0])
    n += 1

    seg1 = [0] * (1 << (n.bit_length() + 1))
    seg2 = [0] * (1 << (n.bit_length() + 1))
    last_x = lines[0][0]

    for x, y1, y2, flag in lines:
        dx = x - last_x
        area += dx * seg2[1]
        update(seg1, seg2, 1, n, y1, y2 - 1, 1, flag)
        last_x = x

    print(area)
