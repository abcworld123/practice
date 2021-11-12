import sys
input = sys.stdin.readline

arr = []
M = int(input())
while 1:
    L, R = map(int, input().split())
    if L == 0 and R == 0: break
    if L > R: L, R = R, L
    if R <= 0 or M <= L: continue
    arr.append((L, R))

if not arr: print(0); exit()
arr.sort(key=lambda x: (x[0], -x[1]))
ans = 0
start, end = 0, 0
next_s, next_e = 0, 0

for i in range(len(arr)):
    to = arr[i]
    if end < to[0]: start, end = next_s, next_e; ans += 1
    if to[0] <= end:
        if M <= to[1]: ans += 1; break
        elif next_e <= to[1]: next_s, next_e = to
else: print(0); exit()

print(ans)
