import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]
trie = {}
_max = 0
ans = []

for word in arr:
    cur = trie
    for lv, c in enumerate(word, start=1):
        if c not in cur:
            cur[c] = [{}, [word], 1]
        else:
            cur[c][1].append(word)
            cur[c][2] += 1
            if _max < lv:
                ans = cur[c][1]
                _max = lv
        cur = cur[c][0]

print(ans[0])
print(ans[1])
