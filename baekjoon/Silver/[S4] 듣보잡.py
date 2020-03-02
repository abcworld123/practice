import sys
s = sys.stdin.readlines()
N, M = map(int, s[0].split())
d, b = set(s[1: N + 1]), set(s[N + 1:])
ans = sorted(d & b)
print(len(ans))
for a in ans: print(a, end='')
