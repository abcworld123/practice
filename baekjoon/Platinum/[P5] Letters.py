import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(input().rstrip())
pair = list(input().rstrip())

dic = defaultdict(list)
for i in range(1, N + 1):
    dic[pair[N - i]].append(i)

fw = [0] * (N + 2)
ans = 0

for x in arr:
    ch = dic[x].pop()
    i, j = ch - 1, ch
    while i: ans += fw[i]; i -= i & -i
    while j <= N: fw[j] += 1; j += j & -j

print(ans)
