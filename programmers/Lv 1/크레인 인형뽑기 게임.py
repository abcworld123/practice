def solution(board, moves):
    answer = 0
    stack = []
    for x in moves:
        x -= 1
        for y in range(len(board)):
            if board[y][x]:
                stack.append(board[y][x])
                board[y][x] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer
