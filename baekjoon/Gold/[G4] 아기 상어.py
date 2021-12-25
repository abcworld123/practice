N = int(input())
arr = [[99] * (N + 2)]
shark = []
size, eat, ans = 2, 0, 0

for i in range(1, N + 1):
    arr.append([99] + list(map(int, input().split())) + [99])
    if not shark and 9 in arr[-1]:
        idx = arr[-1].index(9)
        shark = (i, idx)
        arr[i][idx] = 0
arr.append([99] * (N + 2))

while 1:
    q = [[shark]]
    visited = [[False] * (N + 2) for _ in range(N + 2)]
    visited[shark[0]][shark[1]] = True
    for move, qq in enumerate(q, start=1):
        nqq = []
        for y, x in qq:
            for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if not visited[yy][xx] and arr[yy][xx] <= size:
                    visited[yy][xx] = True
                    nqq.append((yy, xx))
        if nqq:
            q.append(nqq)
            eatable = [(y, x) for y, x in nqq if 0 < arr[y][x] < size]
            if eatable:
                y, x = min(eatable)
                shark = (y, x)
                arr[y][x] = 0
                ans += move
                eat += 1
                if size == eat:
                    size += 1
                    eat = 0
                break
    else: break

print(ans)
