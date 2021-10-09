def solution(n, computers):
    answer = n
    graph = {x: set() for x in range(n)}

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].add(j)
                graph[j].add(i)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i] & graph[j]:
                union = graph[i] | graph[j]
                graph[i], graph[j] = union, union
                answer -= 1
                break
