import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

while 1:
    l = input()
    if l[0] == 48: break
    N, M = map(int, l.split())
    arr = [0] + [x + 100001 for x in map(int, input().split())]
    cnt = [0] * 200002
    rank = [0] * 100001

    sqrtN = 600
    queries = [(*map(int, input().split()), i) for i in range(M)]
    queries.sort(key=lambda x: (x[0] // sqrtN, x[1]))
    ans = [0] * len(queries)
    s, e, cur = 0, 0, 0

    for a, b, i in queries:
        while a < s:
            s -= 1
            cnt[arr[s]] += 1
            x = cnt[arr[s]]
            rank[x - 1] -= 1
            rank[x] += 1
            cur = max(cur, x)
        while e < b:
            e += 1
            cnt[arr[e]] += 1
            x = cnt[arr[e]]
            rank[x - 1] -= 1
            rank[x] += 1
            cur = max(cur, x)
        while s < a:
            x = cnt[arr[s]]
            cnt[arr[s]] -= 1
            rank[x] -= 1
            rank[x - 1] += 1
            if cur == x and rank[x] == 0: cur -= 1
            s += 1
        while b < e:
            x = cnt[arr[e]]
            cnt[arr[e]] -= 1
            rank[x] -= 1
            rank[x - 1] += 1
            if cur == x and rank[x] == 0: cur -= 1
            e -= 1
        ans[i] = cur

    os.write(1, '\n'.join(map(str, ans)).encode())
    os.write(1, b'\n')
