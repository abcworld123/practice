import sys

graph_all = [list(map(int, x.split())) + [0] for x in sys.stdin.readlines()]
graph_all.pop()

for graph in graph_all:
    graph, stack, max_area = graph[1:], [[0, 0]], 0
    for i in range(len(graph)):
        if stack[-1][0] == graph[i]: continue
        elif stack[-1][0] < graph[i]: stack.append([graph[i], i])
        else:
            while stack[-1][0] != graph[i]:
                area = stack[-1][0] * (i - stack[-1][1])
                if area > max_area: max_area = area
                if stack[-2][0] < graph[i]: stack[-1][0] = graph[i]
                else: stack.pop()
    print(max_area)
