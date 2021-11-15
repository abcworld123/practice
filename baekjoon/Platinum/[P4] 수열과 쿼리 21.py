import sys
input = sys.stdin.readline


N = int(input())
arr = [0] + list(map(int, input().split()))
arr2 = [0] + [arr[i] - arr[i - 1] for i in range(1, N + 1)]
fw = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i - (i & -i), i):
        fw[i] += arr2[j + 1]

for i in range(int(input())):
    line = tuple(map(int, input().split()))
    if line[0] == 1:
        i, j, x = line[1], line[2] + 1, line[3]
        while i <= N: fw[i] += x; i += i & -i
        while j <= N: fw[j] -= x; j += j & -j
    else:
        i, summ = line[1], 0
        while i: summ += fw[i]; i -= i & -i
        print(summ)
