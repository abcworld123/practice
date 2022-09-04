import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [['X'] * (C + 2)] + [['X'] + list(input().rstrip()) + ['X'] for _ in range(R)] + [['X'] * (C + 2)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
bq, wq = [], []
ans = 0

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if arr[i][j] == 'S': bq.append((i, j))
        elif arr[i][j] == '*': wq.append((i, j))

while bq:
    ans += 1
    new_bq, new_wq = [], []
    for i, j in wq:
        for dy, dx in d:
            y, x = i + dy, j + dx
            if arr[y][x] == '.':
                arr[y][x] = '@'
                new_wq.append((y, x))
    for i, j in bq:
        for dy, dx in d:
            y, x = i + dy, j + dx
            if arr[y][x] == 'D':
                print(ans)
                exit()
            elif arr[y][x] == '.':
                arr[y][x] = '@'
                new_bq.append((y, x))
    bq, wq = new_bq, new_wq

print('KAKTUS')
