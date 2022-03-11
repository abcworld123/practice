import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

W, H, K = map(int, input().split())
H_W = H + W
ans = [[''] * W for _ in range(H)]
sq = [[0] * (W + 1) for _ in range(H + 1)]
dia = [[0] * H_W for _ in range(H_W)]

for q in (list(map(int, input().split())) for _ in range(K)):
    if q[0] == 1:
        px, py, qx, qy = q[1:]
        qx += 1; qy += 1
        sq[py][px] += 1
        sq[py][qx] += -1
        sq[qy][px] += -1
        sq[qy][qx] += 1
    else:
        _px, _py, r = q[1:]
        px = H - 1 + _px - _py - r
        py = _px + _py - r
        qx = px + 2 * r + 1
        qy = py + 2 * r + 1
        dia[py][px] += 1
        dia[py][qx] += -1
        dia[qy][px] += -1
        dia[qy][qx] += 1

for i in range(H):
    for j in range(1, W):
        sq[i][j] += sq[i][j - 1]

for i in range(1, H):
    for j in range(W):
        sq[i][j] += sq[i - 1][j]

for i in range(1, H_W - 1):
    for j in range(2, H_W - 1):
        dia[i][j] += dia[i][j - 1]

for i in range(2, H_W - 1):
    for j in range(1, H_W):
        dia[i][j] += dia[i - 1][j]

for y in range(H):
    for x in range(W):
        ans[y][x] = '#' if (sq[y][x] + dia[x + y][H - 1 + x - y]) & 1 else '.'

for i in range(H):
    sys.stdout.write(''.join(ans[i]))
    sys.stdout.write('\n')
