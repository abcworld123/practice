import sys
input = sys.stdin.readline


def init(fwtree, N, arr):
    for i in range(1, N + 1):
        for j in range(i - (i & -i), i):
            fwtree[i] += arr[j + 1]
    return fwtree


def summ(fwtree, i):
    total = 0
    while i:
        total += fwtree[i]
        i -= i & -i
    return total


def update(fwtree, arr, N, i, diff):
    arr[i] += diff
    while i <= N:
        fwtree[i] += diff
        i += i & -i


N = int(input())
arr = [0] + list(map(int, input().split()))
fwtree = [0] * (N + 1)
init(fwtree, N, arr)
query1, query2 = [None], []

for i in range(int(input())):
    q = tuple(map(int, input().split()))
    if q[0] == 1: query1.append(q)
    else: query2.append((q, i))

query2.sort(key=lambda x: x[0][1])
q2cur = 0
ans = []

for i in range(len(query1)):
    if i > 0: update(fwtree, arr, N, query1[i][1], query1[i][2] - arr[query1[i][1]])
    while q2cur < len(query2) and query2[q2cur][0][1] <= i:
        ans.append((query2[q2cur][1], summ(fwtree, query2[q2cur][0][3]) - summ(fwtree, query2[q2cur][0][2] - 1)))
        q2cur += 1

for x in sorted(ans, key=lambda x: x[0]): print(x[1])
