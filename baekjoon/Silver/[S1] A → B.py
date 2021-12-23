A, B = map(int, input().split())
visited = {B}
q = [(B, 1)]

for x, c in q:
    if x == A: print(c); exit()
    if x & 1 == 0:
        n1 = x >> 1
        if n1 not in visited and n1 >= A:
            visited.add(n1)
            q.append((n1, c + 1))
    if x % 10 == 1:
        n2 = x // 10
        if n2 not in visited and n2 >= A:
            visited.add(n2)
            q.append((n2, c + 1))

print(-1)
