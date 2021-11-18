import sys
input = sys.stdin.readline


def init(fwtree, N, arr):
    for i in range(1, N + 1):
        for j in range(i - (i & -i), i):
            fwtree[i] += arr[j + 1]

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


N, Q = map(int, input().split())
arr = list(map(int, input().split()))
odd = [0] + arr[::2]
even = [0] + arr[1::2]
n_odd, n_even = len(odd) - 1, len(even) - 1
fw_odd = [0] * (n_odd + 1)
fw_even = [0] * (n_even + 1)
init(fw_odd, n_odd, odd)
init(fw_even, n_even, even)

for i in range(Q):
    op, a, b = map(int, input().split())
    if op == 2:
        if a & 1: update(fw_odd, n_odd, (a >> 1) + 1, b)
        else: update(fw_even, n_even, a >> 1, b)
    else:
        lo, ro, le, re = a >> 1, (b + 1) >> 1, (a - 1) >> 1, b >> 1
        sum_odd = (summ(fw_odd, ro) - summ(fw_odd, lo)) if lo < ro else 0
        sum_even = (summ(fw_even, re) - summ(fw_even, le)) if le < re else 0
        print(abs(sum_odd - sum_even))
