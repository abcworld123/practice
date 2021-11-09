import sys
input = sys.stdin.readline

N = int(input())
arr = (tuple((x, x) for x in map(int, input().split())))

for i in range(N - 1):
    r, g, b = map(int, input().split())
    _r, _g, _b = arr[0], arr[1], arr[2]
    arr = ((min(_r[0], _g[0]) + r, max(_r[1], _g[1]) + r), (min(_r[0], _g[0], _b[0]) + g, max(_r[1], _g[1], _b[1]) + g), (min(_g[0], _b[0]) + b, max(_g[1], _b[1]) + b))

print(max(x[1] for x in arr), min(x[0] for x in arr))
