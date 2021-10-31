from collections import deque

N, K = map(int, input().split())
if N == K: print(0); exit()
visited = [0] * 500001
visited[N] = 2
ds = [K, -1]  # dongsang
queue = deque([[N, 0]])

while queue:
    x, step = queue.popleft()
    if ds[1] != step:
        ds[0] += step
        ds[1] = step
        if ds[0] > 500000: print(-1); exit()
        if (~step & 1 and visited[ds[0]] & 2) or (step & 1 and visited[ds[0]] & 1): print(step); exit()

    for to in (x - 1, x + 1, x * 2):
        if to < 0 or to > 500000: continue
        if visited[to] & 1 == 0 and (step + 1) & 1 == 1: queue.append([to, step + 1]); visited[to] |= 1
        if visited[to] & 2 == 0 and (step + 1) & 1 == 0: queue.append([to, step + 1]); visited[to] |= 2

print(-1)
