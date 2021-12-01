from collections import deque

for T in range(int(input())):
    N, M = map(int, input().split())
    s = list(map(int, input().split()))
    q = deque(enumerate(s))
    s.sort()
    cnt = 1
    while 1:
        if q[0][1] == s[-1]:
            if q[0][0] == M: print(cnt); break
            q.popleft()
            s.pop()
            cnt += 1
        else:
            q.append(q.popleft())
