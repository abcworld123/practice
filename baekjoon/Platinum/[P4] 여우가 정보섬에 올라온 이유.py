import sys
from collections import defaultdict
input = sys.stdin.readline

def summ(fwtree, i):
    total = 0
    while i:
        total += fwtree[i]
        i -= i & -i
    return total

def update(fwtree, N, i, diff):
    while i <= N:
        fwtree[i] += diff
        i += i & -i


N = int(input())
dic = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    dic[b].append(a + 200001)

fw = [0] * 400002
ans = 0

for y in sorted(dic.keys(), reverse=True):
    arr = sorted(dic[y])
    for x in arr: ans = (ans + (summ(fw, x - 1) * (summ(fw, 400001) - summ(fw, x)))) % 1000000007
    for x in arr: update(fw, 400001, x, 1)

print(ans)
