q = [(1, 0)]
arr = list(range(106))
dice = tuple(range(1, 7))
visited = [False] * 106
visited[1] = True

for _ in range(sum(map(int, input().split()))):
    a, b = map(int, input().split())
    arr[a] = b

for x, c in q:
    if x == 100: print(c); break
    if x > 100: continue
    for n in dice:
        if not visited[x + n]:
            q.append((arr[x + n], c + 1))
            visited[x + n] = True
