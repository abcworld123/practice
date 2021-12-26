import sys
input = sys.stdin.buffer

N = int(input.readline())
arr = list(map(int, input))
if N <= 2: print(sum(arr)); exit()
dp = [0, (arr[0], arr[0]), (arr[1], arr[0] + arr[1]), (arr[0] + arr[2], arr[1] + arr[2])]

for i in range(3, N): dp.append((max(max(dp[-3]), max(dp[-2])) + arr[i], dp[-1][0] + arr[i]))
print(max(max(dp[-2]), max(dp[-1])))
