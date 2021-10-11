def solution(arrows):
    answer = 0
    cur = (0, 0)
    graph = {'0 0': set()}
    _dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    x_check = {1: (-1, 3), 3: (1, 1), 5: (1, 7), 7: (-1, 5)}

    for d in arrows:
        to = (cur[0] + _dir[d][0], cur[1] + _dir[d][1])
        cur_str, to_str = f'{cur[0]} {cur[1]}', f'{to[0]} {to[1]}'
        x_str = f'{cur[0] + x_check[d][0] if d & 1 else 0} {cur[1]}'

        if d & 1 and d not in graph[cur_str] and x_str in graph and x_check[d][1] in graph[x_str]: answer += 1
        if to_str not in graph: graph[to_str] = set()
        elif d not in graph[cur_str]: answer += 1

        graph[cur_str].add(d)
        graph[to_str].add((d + 4) % 8)
        cur = to

    return answer
