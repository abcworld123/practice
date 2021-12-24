def bfs():
    A, B = map(int, input().split())
    visited = [False] * 10000
    visited[A] = 0
    q = [(A, '')]
    for x, op in q:
        D = x * 2 % 10000
        S = x - 1 if x != 0 else 9999
        L = (x % 1000) * 10 + (x // 1000)
        R = (x // 10) + (x % 10) * 1000
        for _x, _op in ((D, op + 'D'), (S, op + 'S'), (L, op + 'L'), (R, op + 'R')):
            if not visited[_x]:
                if _x == B: print(_op); return
                q.append((_x, _op))
                visited[_x] = True

for T in range(int(input())): bfs()
