import sys
n = int(sys.stdin.readline()) + 1
graph = list(map(int, sys.stdin)) + [0]
stack = [[0, 0]]
max_area = 0

for i in range(n):
    if stack[-1][0] == graph[i]: continue
    elif stack[-1][0] < graph[i]: stack.append([graph[i], i])
    else:
        while stack[-1][0] != graph[i]:
            area = stack[-1][0] * (i - stack[-1][1])
            if area > max_area: max_area = area
            if stack[-2][0] < graph[i]: stack[-1][0] = graph[i]
            else: stack.pop()

print(max_area)
