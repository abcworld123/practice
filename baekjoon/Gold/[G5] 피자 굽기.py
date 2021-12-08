import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

D, N = map(int, input().split())
arr = list(map(int, input().split()))
pizzas = list(map(int, input().split()))
stack = [[arr[0], 0]]
i = 0

for i in range(len(arr)):
    if arr[i] < stack[-1][0]:
        stack[-1][1] = i - stack[-1][1]
        stack.append([arr[i], i])
stack[-1][1] = D - stack[-1][1]
top = len(stack) - 1

for p in pizzas:
    while top >= 0 and stack[top][0] < p: top -= 1
    if top == -1: print(0); exit()
    stack[top][1] -= 1
    if stack[top][1] == 0: top -= 1
print(sum(stack[i][1] for i in range(top + 1)) + 1)
