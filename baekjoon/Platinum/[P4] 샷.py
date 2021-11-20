import sys
input = sys.stdin.readline

def init(seg, s, e, i):
    m, ch = (s + e) >> 1, i << 1
    seg[i] = (init(seg, s, m, ch) if s != m else 1) + (init(seg, m + 1, e, ch + 1) if m + 1 != e else 1)
    return seg[i]


floor = 3000001
N = int(input())
costs = [0] * (floor + 1)
seg = [1] * (1 << (floor.bit_length() + 1))
top = [0] * N
init(seg, 1, floor, 1)

for score in [1, 2, 5]:
    arr = tuple(map(int, input().split()))
    for i in range(N):
        costs[top[i] + 1] += score
        costs[top[i] + arr[i] + 1] -= score
        top[i] += arr[i]

for i in range(1, floor):
    costs[i] += costs[i - 1]

input()
for k in map(int, input().split()):
    s, e, i = 1, floor, 1
    while s != e:
        seg[i] -= 1
        m, ch = (s + e) >> 1, i << 1
        if k <= seg[ch]: e = m; i = ch
        else: s = m + 1; k -= seg[ch]; i = ch + 1
    seg[i] -= 1
    val = costs[s]
    sys.stdout.write(str(val) + '\n')
