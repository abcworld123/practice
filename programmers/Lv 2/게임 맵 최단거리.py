def solution(maps):
    n, m = len(maps), len(maps[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(0, 0, 1)]
    maps[0][0] = 0

    while queue:
        y, x, count = queue.pop(0)
        for d in dirs:
            _y, _x = y + d[0], x + d[1]
            if 0 <= _y < n and 0 <= _x < m and maps[_y][_x]:
                if _y == n - 1 and _x == m - 1: return count + 1
                queue.append((_y, _x, count + 1))
                maps[_y][_x] = 0
    return -1
