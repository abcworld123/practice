import sys
input = sys.stdin.readline

def init(s, e, i):
    if s == e: seg[i] = arr[s]
    else:
        m, ch = (s + e) >> 1, i << 1
        seg[i] = init(s, m, ch) + init(m + 1, e, ch + 1)
    return seg[i]

def summ(s, e, l, r, i):
    if lz[i]: propagation(s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    return summ(s, m, l, r, ch) + summ(m + 1, e, l, r, ch + 1)

def update(s, e, l, r, i, d):
    if lz[i]: propagation(s, e, i)
    if e < l or r < s: return
    if s == e: seg[i] += d
    elif l <= s and e <= r:
        ch = i << 1
        seg[i] += (e - s + 1) * d
        lz[ch] += d
        lz[ch + 1] += d
    else:
        m, ch = (s + e) >> 1, i << 1
        update(s, m, l, r, ch, d)
        update(m + 1, e, l, r, ch + 1, d)
        seg[i] = seg[ch] + seg[ch + 1]

def propagation(s, e, i):
    ch = i << 1
    seg[i] += (e - s + 1) * lz[i]
    if s != e:
        lz[ch] += lz[i]
        lz[ch + 1] += lz[i]
    lz[i] = 0


N, M = map(int, input().split())
area, arr = {}, [0]

x, y, d = map(int, input().split())
if x <= y:
    for i in range(x, y + 1): area[i] = 1
    arr.append(d)
else:
    for i in range(y, N + 1): area[i] = 1
    for i in range(1, x + 1): area[i] = 1
    arr.append(d)

for m in range(2, M + 1):
    x, y, d = map(int, input().split())
    for i in range(x, y + 1): area[i] = m
    arr.append(d)

seg = [0] * (1 << (M.bit_length() + 1))
lz = seg[:]
init(1, M, 1)

while 1:
    cmd = tuple(map(int, input().split()))
    if cmd[0] == 0: break
    if cmd[0] == 1:
        if area[cmd[1]] <= area[cmd[2]]:
            sys.stdout.write(str(summ(1, M, area[cmd[1]], area[cmd[2]], 1)) + '\n')
        else:
            sys.stdout.write(str(summ(1, M, area[cmd[1]], M, 1) + summ(1, M, 1, area[cmd[2]], 1)) + '\n')
    else:
        if area[cmd[1]] <= area[cmd[2]]:
            update(1, M, area[cmd[1]], area[cmd[2]], 1, cmd[3])
        else:
            update(1, M, area[cmd[1]], M, 1, cmd[3])
            update(1, M, 1, area[cmd[2]], 1, cmd[3])

# 비재귀 세그트리 구현해보기
