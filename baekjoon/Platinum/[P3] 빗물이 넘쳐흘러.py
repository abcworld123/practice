import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split())) + [0]
stack, water, can = [], 0, 0

for x in arr:
    cur = [x, 1, 0]
    if not stack: stack.append(cur)
    elif stack[-1][0] < x: stack.append(cur)
    elif stack[-1][0] == x: stack[-1][1] += 1
    else:
        cur[2] = 1
        if stack[-1][2] == 0 and can + 1 == Q: print(water); exit()
        can += 1
        while stack and stack[-1][0] > x:
            pop = stack.pop()
            cur[1] += pop[1]
            water += (pop[0] - x) * pop[1]
            can -= pop[2]
        stack.append(cur)

print(-1)
