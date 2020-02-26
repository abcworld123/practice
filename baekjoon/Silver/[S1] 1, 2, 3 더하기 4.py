import sys

input()
arr = [[0, 0], [0, 1], [1, 2], [1, 3]]
max_index = 3

for n in map(int, sys.stdin.readlines()):
    if n > max_index:
        for i in range(max_index + 1, n + 1): arr.append([arr[i - 2][0] + 1, arr[i - 2][0] + arr[i - 3][1] + 2])
        max_index = n
    print(arr[n][1])
