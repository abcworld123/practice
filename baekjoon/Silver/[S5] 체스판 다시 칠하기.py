def board_check(a, b, board):
    line = "WBWBWBWB"
    count = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if line[j] == board[a + i][b + j] and i % 2 == 0: count += 1
            if line[j] != board[a + i][b + j] and i % 2 == 1: count += 1
    return min(count, 64 - count)


m, n = map(int, input().split())
min_val = 64
board = []
for i in range(0, m): board += [input()]

for i in range(0, m - 7):
    for j in range(0, n - 7):
        min_val = min(min_val, board_check(i, j, board))
print(min_val)
