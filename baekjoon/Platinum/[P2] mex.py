import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size))

N, M = map(int, input.readline().split())
ans = __pypy__.builders.StringBuilder()
trie = [None, None, [0, 0]]
xor = 0

for x in set(map(int, input.readline().split())):
    cur, b = trie, 262144
    while b:
        xb = 1 if x & b else 0
        cur[2][xb] += 1
        cur[xb] = cur[xb] if cur[xb] else [None, None, [0, 0]]
        cur = cur[xb]
        b >>= 1

for x in map(int, input.read().split()):
    cur, b, c = trie, 262144, 0
    xor ^= x
    while b:
        xb = 1 if xor & b else 0
        if not cur or not cur[xb]:
            c += ((b << 1) - 1) & xor
            break
        to = xb if cur[2][xb] != b else xb ^ 1
        if to: c += b
        cur = cur[to]
        b >>= 1
    ans.append(str(c ^ xor) + '\n')

os.write(1, ans.build().encode())
