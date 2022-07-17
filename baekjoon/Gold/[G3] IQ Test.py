def p(x):
    print(x)
    exit()

N = int(input())
arr = list(map(int, input().split()))

if N == 1: p('A')
elif arr[0] == arr[1]:
    if len(set(arr)) == 1: p(arr[0])
    else: p('B')
elif N == 2: p('A')

a = (arr[1] - arr[2]) / (arr[0] - arr[1])
if a != int(a): p('B')
a = int(a)
b = arr[1] - arr[0] * a

for i in range(2, N - 1):
    if arr[i] * a + b != arr[i + 1]: p('B')
p(arr[-1] * a + b)
