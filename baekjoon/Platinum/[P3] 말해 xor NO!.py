import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M, K = map(int, input().split())
trie = [None, None, [0, 0]]
ans = 0

for x in map(int, input().split()):
    cur, b = trie, 536870912
    while b:
        xb = 1 if x & b else 0
        cur[2][xb] += 1
        cur[xb] = cur[xb] if cur[xb] else [None, None, [0, 0]]
        cur = cur[xb]
        b >>= 1

for x in map(int, input().split()):
    cur, b = trie, 536870912
    while b:
        kb = 1 if K & b else 0
        xb = 1 if x & b else 0
        ans += cur[2][xb] if kb else 0
        to = kb ^ xb
        if not cur[to]: break
        cur = cur[to]
        b >>= 1

print(ans)
