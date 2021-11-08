import sys
input = sys.stdin.readline


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


N, Q = map(int, input().split())
arr = [0] * (N + 1)
fwtree = arr[:]

for i in range(Q):
    op, a, b = map(int, input().split())
    if op == 1: update(fwtree, arr, N, a, b)
    else: print(summ(fwtree, b) - summ(fwtree, a - 1))
