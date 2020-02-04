arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101): arr += [arr[i - 5] + arr[i - 1]]
for i in range(int(input())): print(arr[int(input())])
