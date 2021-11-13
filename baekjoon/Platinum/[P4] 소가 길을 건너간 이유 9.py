import sys
input = sys.stdin.readline


def summ(fwtree, i):
    total = 0
    while i:
        total += fwtree[i]
        i -= i & -i
    return total


def update(fwtree, N, i, val):
    while i <= N:
        fwtree[i] += val
        i += i & -i


N = int(input()) * 2
end = [0] * (N // 2 + 1)
arr = [0] + [int(input()) for _ in range(N)]
for i in range(1, len(arr)): end[arr[i]] = i

fwtree = [0] * (N + 1)
ans = 0

for i in range(1, N + 1):
    if i == end[arr[i]]: continue
    ans += abs(summ(fwtree, end[arr[i]]) - summ(fwtree, i - 1))
    update(fwtree, N, i, 1)
    update(fwtree, N, end[arr[i]], -1)

print(ans)
