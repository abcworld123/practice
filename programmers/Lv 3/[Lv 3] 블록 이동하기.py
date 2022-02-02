def solution(board):
    N = len(board)
    board = [[1] * (N + 2)] + [[1] + b + [1] for b in board] + [[1] * (N + 2)]
    visited = [[[False] * 2 for _ in range(N + 2)] for _ in range(N + 2)]
    q = [(1, 1, 0, 0)]  # y, x, s, m (s - 0: 가로, 1: 세로)
    visited[1][1][0] = True

    for y, x, s, m in q:
        if (y == N - 1 and x == N) or (y == N and x == N - 1): return m
        if s == 0:
            if board[y - 1][x] == 0 and board[y - 1][x + 1] == 0:
                if not visited[y - 1][x][0]:
                    visited[y - 1][x][0] = True
                    q.append((y - 1, x, 0, m + 1))
                if not visited[y - 1][x][1]:
                    visited[y - 1][x][1] = True
                    q.append((y - 1, x, 1, m + 1))
                if not visited[y - 1][x + 1][1]:
                    visited[y - 1][x + 1][1] = True
                    q.append((y - 1, x + 1, 1, m + 1))

            if board[y][x + 2] == 0 and not visited[y][x + 1][0]:
                visited[y][x + 1][0] = True
                q.append((y, x + 1, 0, m + 1))

            if board[y + 1][x] == 0 and board[y + 1][x + 1] == 0:
                if not visited[y + 1][x][0]:
                    visited[y + 1][x][0] = True
                    q.append((y + 1, x, 0, m + 1))
                if not visited[y][x][1]:
                    visited[y][x][1] = True
                    q.append((y, x, 1, m + 1))
                if not visited[y][x + 1][1]:
                    visited[y][x + 1][1] = True
                    q.append((y, x + 1, 1, m + 1))

            if board[y][x - 1] == 0 and not visited[y][x - 1][0]:
                visited[y][x - 1][0] = True
                q.append((y, x - 1, 0, m + 1))

        else:
            if board[y - 1][x] == 0 and not visited[y - 1][x][1]:
                visited[y - 1][x][1] = True
                q.append((y - 1, x, 1, m + 1))

            if board[y][x + 1] == 0 and board[y + 1][x + 1] == 0:
                if not visited[y][x + 1][1]:
                    visited[y][x + 1][1] = True
                    q.append((y, x + 1, 1, m + 1))
                if not visited[y][x][0]:
                    visited[y][x][0] = True
                    q.append((y, x, 0, m + 1))
                if not visited[y + 1][x][0]:
                    visited[y + 1][x][0] = True
                    q.append((y + 1, x, 0, m + 1))

            if board[y + 2][x] == 0 and not visited[y + 1][x][1]:
                visited[y + 1][x][1] = True
                q.append((y + 1, x, 1, m + 1))

            if board[y][x - 1] == 0 and board[y + 1][x - 1] == 0:
                if not visited[y][x - 1][1]:
                    visited[y][x - 1][1] = True
                    q.append((y, x - 1, 1, m + 1))
                if not visited[y][x - 1][0]:
                    visited[y][x - 1][0] = True
                    q.append((y, x - 1, 0, m + 1))
                if not visited[y + 1][x - 1][0]:
                    visited[y + 1][x - 1][0] = True
                    q.append((y + 1, x - 1, 0, m + 1))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
