import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = [(i, j) for i in range(1, N - 1) for j in range(1, M - 1) if arr[i][j]]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
day = 0

while q:
    day += 1
    nq = []
    narr = [x[:] for x in arr]
    for i, j in q:
        for dy, dx in d:
            if arr[i + dy][j + dx] <= 0:
                narr[i][j] -= 1
        if narr[i][j] > 0:
            nq.append((i, j))

    if not nq: break
    if (len(q) != len(nq)):
        q = [(nq[0][0], nq[0][1])]
        arr = [x[:] for x in narr]
        arr[q[0][0]][q[0][1]] = 0
        for i, j in q:
            for dy, dx in d:
                y, x = i + dy, j + dx
                if arr[y][x] > 0:
                    q.append((y, x))
                    arr[y][x] = 0
        if len(q) != len(nq):
            print(day)
            exit()

    arr = narr
    q = nq

print(0)
