import sys
input = sys.stdin.readline

def ccw(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
points = [tuple(map(int, input().split())) for _ in range(3)]
arr += [arr[0], arr[1]]
count = [0, 0, 0]

for i in range(3):
    p = points[i]
    p2 = (2000000000, p[1])
    for j in range(len(arr) - 2):
        a, b = arr[j], arr[j + 1]
        if p == a or p == b: count[i] = 1; break
        elif ccw(a, b, p) == 0:
            if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]): count[i] = 1; break
        elif p[1] == b[1]:
            if p[0] < b[0] and ccw(p, b, a) * ccw(p, b, arr[j + 2]) < 0: count[i] += 1
        elif p[1] == a[1]: continue
        else:
            if ccw(p, p2, a) * ccw(p, p2, b) < 0 and ccw(a, b, p) * ccw(a, b, p2) < 0: count[i] += 1

for x in count: print(x & 1)
