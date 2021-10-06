from collections import deque, Counter

def solution(n, edge):
    dist = {x: -1 for x in range(1, n + 1)}
    graph = {x: [] for x in range(1, n + 1)}
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dist[1] = 0
    queue = deque([(1, 0)])
    while queue:
        cv, cdist = queue.popleft()
        for v in graph[cv]:
            if dist[v] == -1:
                dist[v] = cdist + 1
                queue.append((v, dist[v]))

    return Counter(dist.values())[max(dist.values())]
