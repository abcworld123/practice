def bfs(arr):
    area = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j]:
                area += 1
                c = arr[i][j]
                arr[i][j] = ''
                q = [(i, j)]
                for a, b in q:
                    for y, x in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
                        if arr[y][x] == c:
                            arr[y][x] = ''
                            q.append((y, x))
    return area

N = int(input())
arr1 = [[''] * (N + 2)] + [[''] + list(input()) + [''] for _ in range(N)] + [[''] * (N + 2)]
arr2 = [[c if c != 'G' else 'R' for c in line] for line in arr1]
area1, area2 = 0, 0

print(bfs(arr1), bfs(arr2))
