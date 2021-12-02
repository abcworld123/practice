import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def update(seg, comp, s, e, l, r, i, f):
    ch = i << 1
    if l <= s and e <= r:
        seg[i][0] += (comp[e + 1] - comp[s]) * f
    else:
        m = (s + e) >> 1
        if l <= m: update(seg, comp, s, m, l, r, ch, f)
        if m + 1 <= r: update(seg, comp, m + 1, e, l, r, ch + 1, f)

    if seg[i][0]: seg[i][1] = comp[e + 1] - comp[s]
    elif s == e: seg[i][1] = 0
    else: seg[i][1] = seg[ch][1] + seg[ch + 1][1]


lines = []
comp_from = set()

for _ in range(int(input())):
    x1, x2, y1, y2 = map(int, input().split())
    lines.append((x1, y1, y2, 1))
    lines.append((x2, y1, y2, -1))
    comp_from.add(y1)
    comp_from.add(y2)

n = len(comp_from)
comp_from = [0] + sorted(comp_from)
comp_to = {comp_from[k]: k for k in range(1, len(comp_from))}
seg = [[0, 0] for _ in range((1 << (n.bit_length() + 1)))]
lines.sort(key=lambda x: x[0])
last_x = lines[0][0]
area = 0

for x, y1, y2, flag in lines:
    dx = x - last_x
    area += dx * seg[1][1]
    update(seg, comp_from, 1, n, comp_to[y1], comp_to[y2] - 1, 1, flag)
    last_x = x

print(area)


# y좌표를 압축해서 처리,
# y좌표를 트리에 저장하는 것이 아니라
# 영역의 번호를 저장하는 느낌.
