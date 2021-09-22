dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def go(c, d):
    if c == 'S': return d
    elif c == 'L': return dirs[(dirs.index(d) - 1) % 4]
    elif c == 'R': return dirs[(dirs.index(d) + 1) % 4]

def solution(grid):
    arrows = set()
    answer = []
    len_y, len_x = len(grid), len(grid[0])
    for y in range(len_y):
        for x in range(len_x):
            for dy, dx in dirs:
                answer.append(0)
                cur_y, cur_x = y, x
                while True:
                    dy, dx = go(grid[cur_y][cur_x], (dy, dx))
                    arrow = f'{cur_y},{cur_x},{dy},{dx}'
                    if arrow not in arrows:
                        arrows.add(arrow)
                        answer[-1] += 1
                        cur_y, cur_x = (cur_y + dy) % len_y, (cur_x + dx) % len_x
                    else: break

    return sorted([x for x in answer if x])
