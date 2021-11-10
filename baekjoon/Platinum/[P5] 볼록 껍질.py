import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
start = min(points)

ninf, ok, pinf = [], [], []
for p in points:
    if p[0] - start[0] == 0:
        if p[1] - start[1] < 0: ninf.append(p)
        elif p[1] - start[1] > 0: pinf.append(p)
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

print(len(ans))
