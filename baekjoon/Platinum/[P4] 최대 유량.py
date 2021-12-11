import sys
input = sys.stdin.readline

def bfs(graph, flow, capacity, S, T):
    q = [S]
    path = [-1] * 52
    for cur in q:
        for v in graph[cur]:
            if path[v] == -1 and capacity[cur][v] - flow[cur][v] > 0:
                path[v] = cur
                q.append(v)
                if v == T: return byebye(flow, path, S, T)
    return 0

def byebye(flow, path, S, T):
    cur = T
    water = float('inf')
    while cur != S:
        water = min(water, capacity[path[cur]][cur] - flow[path[cur]][cur])
        cur = path[cur]
    cur = T
    while cur != S:
        flow[path[cur]][cur] += water
        flow[cur][path[cur]] -= water
        cur = path[cur]
    return water


graph = [set() for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]
capacity = [[0] * 52 for _ in range(52)]
_ord = lambda x: ord(x) - 65 if x <= 'Z' else ord(x) - 71

for _ in range(int(input())):
    a, b, c = input().split()
    a, b, c = _ord(a), _ord(b), int(c)
    graph[a].add(b)
    graph[b].add(a)
    capacity[a][b] += int(c)
    capacity[b][a] += int(c)

ans, ret = 0, -1
while ret:
    ret = bfs(graph, flow, capacity, _ord('A'), _ord('Z'))
    ans += ret

print(ans)
