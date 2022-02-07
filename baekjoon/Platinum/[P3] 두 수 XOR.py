import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).read

_, *arr = map(int, input().split())
trie = [None, None, [0, 0]]
ans = 0

for x in arr:
    cur, b = trie, 536870912
    while b:
        xb = 1 if x & b else 0
        cur[2][xb] += 1
        cur[xb] = cur[xb] if cur[xb] else [None, None, [0, 0]]
        cur = cur[xb]
        b >>= 1

for x in arr:
    cur, b, c = trie, 536870912, 0
    while b:
        xb = 1 if x & b else 0
        to = xb ^ 1 if cur[xb ^ 1] else xb
        if to: c += b
        cur = cur[to]
        b >>= 1
    ans = max(ans, c ^ x)

print(ans)

##########################

# set을 이용한 풀이... 뭔소린지 모르겠음
import sys

input = sys.stdin.readline


def BOJ13505():
    n = int(input())
    nums = list(map(int, input().split()))

    maxx = 0
    mask = 0
    se = set()

    for i in range(30, -1, -1):
        mask |= (1 << i)
        newMaxx = maxx | (1 << i)

        for i in range(n):
            se.add(nums[i] & mask)

        for prefix in se:
            if (newMaxx ^ prefix) in se:
                maxx = newMaxx
                break
        se.clear()

    print(maxx)


BOJ13505()
