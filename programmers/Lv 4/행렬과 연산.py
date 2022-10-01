from collections import deque

def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    ver_left = deque([rc[i][0] for i in range(n)])
    ver_right = deque([rc[i][-1] for i in range(n)])
    hor_deques = deque([deque([rc[i][j] for j in range(1, m - 1)]) for i in range(n)])

    for op in operations:
        if op[0] == 'S':
            ver_left.appendleft(ver_left.pop())
            ver_right.appendleft(ver_right.pop())
            hor_deques.appendleft(hor_deques.pop())
        else:
            hor_deques[0].appendleft(ver_left.popleft())
            hor_deques[-1].append(ver_right.pop())
            ver_right.appendleft(hor_deques[0].pop())
            ver_left.append(hor_deques[-1].popleft())

    ans = [[ver_left[i]] + list(hor_deques[i]) + [ver_right[i]] for i in range(n)]
    return ans


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
