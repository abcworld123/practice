N = int(input())
arr = [[0] * (N + 2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0] * (N + 2)]
ans = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j]:
            arr[i][j] = 0
            q = [(i, j)]
            for x, y in q:
                if arr[x][y - 1]: q.append((x, y - 1)); arr[x][y - 1] = 0
                if arr[x][y + 1]: q.append((x, y + 1)); arr[x][y + 1] = 0
                if arr[x - 1][y]: q.append((x - 1, y)); arr[x - 1][y] = 0
                if arr[x + 1][y]: q.append((x + 1, y)); arr[x + 1][y] = 0
            ans.append(len(q))

print(len(ans))
print('\n'.join(map(str, sorted(ans))))
