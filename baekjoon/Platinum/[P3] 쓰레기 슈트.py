import sys, math
input = sys.stdin.readline


def convex_hull(points):
    start = min(points)
    ninf, ok, pinf = [], [], []
    for p in points:
        if p[0] - start[0] == 0:
            if p[1] - start[1] < 0:
                ninf.append(p)
            elif p[1] - start[1] > 0:
                pinf.append(p)
        else: ok.append(p)

    ninf.sort(key=lambda x: x[1])
    ok.sort(key=lambda x: ((x[1] - start[1]) / (x[0] - start[0]), x[0]))
    pinf.sort(key=lambda x: x[1])
    points = ninf + ok + pinf
    ans = [start, points[0]]

    for i in range(1, len(points)):
        while len(ans) >= 2 and (ans[-1][0] - ans[-2][0]) * (points[i][1] - ans[-2][1]) - (ans[-1][1] - ans[-2][1]) * (points[i][0] - ans[-2][0]) <= 0:
            ans.pop()
        ans.append(points[i])

    return ans


case = 1
while 1:
    N = int(input())
    if N == 0: break
    points = convex_hull([list(map(int, input().split())) for _ in range(N)])
    ans = float('inf')

    for i in range(-1, len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if x1 == x2: a, b, c = 1, 0, -x1
        elif y1 == y2: a, b, c = 0, 1, -y1
        else:
            slope = (y2 - y1) / (x2 - x1)
            x0 = x1 - y1 / slope
            y0 = y1 - x1 * slope
            if x0 == 0: a, b, c = slope, -1, 0
            else: a, b, c = y0, x0, -x0 * y0
        dist = max([abs(a * points[k][0] + b * points[k][1] + c) / math.sqrt(a * a + b * b) for k in range(len(points)) if k != i and k != i + 1])
        if dist < ans: ans = dist
    print(f'Case {case}: {math.ceil(ans * 100) / 100.0:.2f}')
    case += 1
