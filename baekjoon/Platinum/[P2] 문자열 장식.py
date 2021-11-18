import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() + 'a' for _ in range(N)]
chs = sum(len(w) - 1 for w in arr)
ans = []

for i in range(chs):
    k = -1
    for j in range(len(arr)):
        if arr[j][0] == 'a': continue
        if k == -1: k = j
        elif arr[j] < arr[k]: k = j
    ans.append(arr[k][0])
    arr[k] = arr[k][1:]

print(''.join(ans))
