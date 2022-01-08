N, K = map(int, input().split())
if N == K: print('0\n1'); exit()
visited = [False] * 100001
visited[N] = True
q = [(N, 0)]
ans = 0

while 1:
    post = []
    v = []
    for x, i in q:
        for xx in (x - 1, x + 1, 2 * x):
            if 0 <= xx <= 100000 and not visited[xx]:
                v.append(xx)
                if xx == K: ans += 1
                post.append((xx, i + 1))
    if ans: print(f'{i + 1}\n{ans}'); break
    for xx in v: visited[xx] = True
    q = post
