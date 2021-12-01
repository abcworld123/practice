import sys
input = sys.stdin.readline

ans, s, cur = [], [0], 0
for _ in range(int(input())):
    x = int(input())
    if s[-1] > x:
        print('NO')
        exit()
    while s[-1] < x:
        s.append(cur := cur + 1)
        ans.append('+')
    s.pop()
    ans.append('-')

sys.stdout.write('\n'.join(ans))
